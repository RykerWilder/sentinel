#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import random
import subprocess
import os
import sys
import argparse
from typing import List, Optional, Tuple


class MACSpoofer:
    """
    Classe per gestire il MAC spoofing su sistemi Unix.
    Permette di cambiare l'indirizzo MAC di un'interfaccia di rete.
    """

    def __init__(self):
        """Inizializza l'oggetto MacSpoofer."""
        self.current_mac = None
        self.interface = None
        self.is_root = os.geteuid() == 0

    def get_interfaces(self) -> List[str]:
        """
        Ottiene la lista delle interfacce di rete disponibili.
        
        Returns:
            List[str]: Lista delle interfacce di rete.
        """
        try:
            # Utilizza 'ip link show' per ottenere le interfacce su sistemi moderni
            result = subprocess.run(['ip', 'link', 'show'], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   check=True)
            
            # Estrae i nomi delle interfacce dall'output
            interfaces = []
            for line in result.stdout.split('\n'):
                if ':' in line and '@' not in line:  # Esclude interfacce virtuali come lo@
                    match = re.search(r'^\d+: ([^:]+):', line.strip())
                    if match:
                        interfaces.append(match.group(1))
            
            return interfaces
            
        except (subprocess.SubprocessError, FileNotFoundError):
            # Fallback per sistemi BSD o più vecchi
            try:
                result = subprocess.run(['ifconfig'], 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE,
                                       text=True,
                                       check=True)
                
                interfaces = []
                for line in result.stdout.split('\n'):
                    if line and not line.startswith(' '):
                        match = re.search(r'^([a-zA-Z0-9]+):', line)
                        if match:
                            interfaces.append(match.group(1))
                
                return interfaces
                
            except (subprocess.SubprocessError, FileNotFoundError):
                print("[!] Impossibile ottenere le interfacce di rete.")
                return []

    def get_current_mac(self, interface: str) -> Optional[str]:
        """
        Ottiene l'indirizzo MAC attuale dell'interfaccia specificata.
        
        Args:
            interface (str): Il nome dell'interfaccia.
            
        Returns:
            Optional[str]: L'indirizzo MAC attuale o None se non trovato.
        """
        try:
            # Prima prova con ip link
            result = subprocess.run(['ip', 'link', 'show', interface], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   check=True)
            
            mac_search = re.search(r'link/ether ([0-9a-f:]{17})', result.stdout)
            if mac_search:
                return mac_search.group(1)
                
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
        
        # Fallback a ifconfig
        try:
            result = subprocess.run(['ifconfig', interface], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   check=True)
            
            # Cerca l'indirizzo MAC in diversi formati possibili
            mac_search = re.search(r'(ether|HWaddr|lladdr) ([0-9a-f:]{17})', result.stdout)
            if mac_search:
                return mac_search.group(2)
                
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
            
        print(f"[!] Impossibile ottenere l'indirizzo MAC per {interface}")
        return None

    def generate_mac(self, vendor_prefix: Optional[str] = None) -> str:
        """
        Genera un indirizzo MAC casuale.
        
        Args:
            vendor_prefix (Optional[str]): Prefisso del venditore (primi 3 byte).
                                         Se None, viene generato casualmente.
            
        Returns:
            str: Un indirizzo MAC casuale.
        """
        if vendor_prefix:
            # Verifica che il vendor prefix sia nel formato corretto
            if not re.match(r'^([0-9a-f]{2}:){2}[0-9a-f]{2}$', vendor_prefix.lower()):
                raise ValueError("Il prefisso del venditore deve essere nel formato XX:XX:XX")
            
            prefix = vendor_prefix.lower()
        else:
            # Genera un prefisso casuale (evitando indirizzi multicast/broadcast)
            byte1 = random.randint(0, 254)
            # Forza il bit locale amministrato (secondo bit del primo byte)
            byte1 = byte1 & 0xFE | 0x02
            prefix = f"{byte1:02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}"
            
        # Genera i restanti 3 byte in modo casuale
        suffix = ":".join(f"{random.randint(0, 255):02x}" for _ in range(3))
        return f"{prefix}:{suffix}"

    def change_mac(self, interface: str, new_mac: Optional[str] = None) -> Tuple[bool, str]:
        """
        Cambia l'indirizzo MAC dell'interfaccia specificata.
        
        Args:
            interface (str): Il nome dell'interfaccia.
            new_mac (Optional[str]): Il nuovo indirizzo MAC. Se None, ne viene generato uno casuale.
            
        Returns:
            Tuple[bool, str]: (Successo, Messaggio)
        """
        if not self.is_root:
            return False, "Devi essere root per cambiare l'indirizzo MAC"
            
        self.interface = interface
        
        # Verifica che l'interfaccia esista
        if interface not in self.get_interfaces():
            return False, f"L'interfaccia {interface} non esiste"
            
        # Ottiene l'indirizzo MAC attuale
        self.current_mac = self.get_current_mac(interface)
        if not self.current_mac:
            return False, f"Impossibile ottenere l'indirizzo MAC attuale per {interface}"
            
        # Se non è specificato un nuovo MAC, ne genera uno casuale
        if not new_mac:
            new_mac = self.generate_mac()
        else:
            # Verifica che il nuovo MAC sia nel formato corretto
            if not re.match(r'^([0-9a-f]{2}:){5}[0-9a-f]{2}$', new_mac.lower()):
                return False, "Il formato MAC non è valido. Usa XX:XX:XX:XX:XX:XX"
                
        try:
            # Disattiva l'interfaccia
            print(f"[*] Disattivazione dell'interfaccia {interface}...")
            subprocess.run(['ip', 'link', 'set', interface, 'down'], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
            # Cambia l'indirizzo MAC
            print(f"[*] Cambiamento dell'indirizzo MAC a {new_mac}...")
            subprocess.run(['ip', 'link', 'set', interface, 'address', new_mac], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
            # Riattiva l'interfaccia
            print(f"[*] Riattivazione dell'interfaccia {interface}...")
            subprocess.run(['ip', 'link', 'set', interface, 'up'], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
        except subprocess.CalledProcessError as e:
            # Se fallisce con ip, prova con ifconfig
            try:
                subprocess.run(['ifconfig', interface, 'down'], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
                subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
                subprocess.run(['ifconfig', interface, 'up'], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
            except subprocess.CalledProcessError as e2:
                error_msg = e2.stderr.decode() if e2.stderr else str(e2)
                return False, f"Errore nel cambiamento dell'indirizzo MAC: {error_msg}"
        
        # Verifica che il MAC sia stato cambiato correttamente
        new_current_mac = self.get_current_mac(interface)
        if new_current_mac.lower() == new_mac.lower():
            return True, f"Indirizzo MAC cambiato con successo da {self.current_mac} a {new_mac}"
        else:
            return False, f"Impossibile verificare il cambio MAC. MAC attuale: {new_current_mac}"

    def restore_mac(self) -> Tuple[bool, str]:
        """
        Ripristina l'indirizzo MAC originale dell'interfaccia.
        
        Returns:
            Tuple[bool, str]: (Successo, Messaggio)
        """
        if not self.is_root:
            return False, "Devi essere root per ripristinare l'indirizzo MAC"
            
        if not self.interface or not self.current_mac:
            return False, "Nessun indirizzo MAC precedente da ripristinare"
            
        try:
            # Disattiva l'interfaccia
            subprocess.run(['ip', 'link', 'set', self.interface, 'down'], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
            # Ripristina l'indirizzo MAC originale
            subprocess.run(['ip', 'link', 'set', self.interface, 'address', self.current_mac], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
            # Riattiva l'interfaccia
            subprocess.run(['ip', 'link', 'set', self.interface, 'up'], 
                          check=True, 
                          stderr=subprocess.PIPE)
            
        except subprocess.CalledProcessError:
            # Se fallisce con ip, prova con ifconfig
            try:
                subprocess.run(['ifconfig', self.interface, 'down'], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
                subprocess.run(['ifconfig', self.interface, 'hw', 'ether', self.current_mac], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
                subprocess.run(['ifconfig', self.interface, 'up'], 
                              check=True, 
                              stderr=subprocess.PIPE)
                              
            except subprocess.CalledProcessError as e:
                error_msg = e.stderr.decode() if e.stderr else str(e)
                return False, f"Errore nel ripristino dell'indirizzo MAC: {error_msg}"
        
        # Verifica che il MAC sia stato ripristinato correttamente
        new_current_mac = self.get_current_mac(self.interface)
        if new_current_mac.lower() == self.current_mac.lower():
            temp_interface = self.interface
            self.interface = None
            self.current_mac = None
            return True, f"Indirizzo MAC dell'interfaccia {temp_interface} ripristinato con successo"
        else:
            return False, f"Impossibile verificare il ripristino MAC. MAC attuale: {new_current_mac}"


    def mac_spoofer_manager(self, args=None):
        """
        Funzione principale per l'utilizzo da riga di comando del MAC spoofer.
        Può essere chiamata come metodo di classe o con argomenti personalizzati.
        
        Args:
            args: Argomenti di riga di comando personalizzati. Se None, usa sys.argv.
        """
        parser = argparse.ArgumentParser(description='Strumento di MAC spoofing per sistemi Unix')
        parser.add_argument('-i', '--interface', help='Interfaccia di rete da utilizzare')
        parser.add_argument('-m', '--mac', help='Indirizzo MAC specifico da utilizzare (opzionale)')
        parser.add_argument('-r', '--random', action='store_true', help='Genera un MAC casuale')
        parser.add_argument('-l', '--list', action='store_true', help='Lista delle interfacce disponibili')
        parser.add_argument('--restore', action='store_true', help='Ripristina l\'indirizzo MAC originale')
        
        args = parser.parse_args(args)
        
        # Controllo se è in esecuzione come root
        if not self.is_root:
            print("[!] Questo script deve essere eseguito come root (sudo).")
            return False
        
        # Lista delle interfacce disponibili
        if args.list:
            interfaces = self.get_interfaces()
            print("\nInterfacce di rete disponibili:")
            for iface in interfaces:
                mac = self.get_current_mac(iface)
                print(f"  - {iface}: {mac if mac else 'MAC non disponibile'}")
            print()
            return True
        
        # Controlla se è stata specificata un'interfaccia
        if not args.interface:
            interfaces = self.get_interfaces()
            if not interfaces:
                print("[!] Nessuna interfaccia disponibile.")
                return False
                
            print("\nSpecifica un'interfaccia tra queste:")
            for iface in interfaces:
                mac = self.get_current_mac(iface)
                print(f"  - {iface}: {mac if mac else 'MAC non disponibile'}")
            print("\nUtilizzo: sudo python3 macspoofer.py -i [interfaccia] [opzioni]\n")
            return False
        
        # Ottiene l'indirizzo MAC attuale
        current_mac = self.get_current_mac(args.interface)
        if current_mac:
            print(f"[*] Indirizzo MAC attuale per {args.interface}: {current_mac}")
        
        # Ripristina l'indirizzo MAC originale
        if args.restore:
            if not self.interface or not self.current_mac:
                print("[!] Nessun indirizzo MAC precedente da ripristinare.")
                print("[!] Il ripristino funziona solo all'interno della stessa sessione.")
                return False
            success, message = self.restore_mac()
            print(f"[{'✓' if success else '✗'}] {message}")
            return success
        
        # Cambia l'indirizzo MAC
        if args.random or args.mac:
            success, message = self.change_mac(args.interface, args.mac)
            print(f"[{'✓' if success else '✗'}] {message}")
            return success
        else:
            print("[!] Specifica --random per generare un MAC casuale o --mac per un MAC specifico.")
            return False