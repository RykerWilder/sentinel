import nmap
from colorama import Style, Fore
from sentinel import print_dynamic_dots
import shutil

class PortBlitz:
    def nmap_port_scan(self, target, ports="1-1000", arguments="-sV"):
        """
        Esegue una scansione delle porte con Nmap.
        
        Args:
            target (str): IP o dominio da scannerizzare (es. "192.168.1.1" o "scanme.nmap.org").
            ports (str): Range di porte (es. "1-1000", "22,80,443").
            arguments (str): Argomenti aggiuntivi per Nmap (es. "-sV" per version detection).
        """
        scanner = nmap.PortScanner()
        print(f"Scanning {Fore.GREEN}{target}{Style.RESET_ALL} on ports {Fore.GREEN}{ports}{Style.RESET_ALL}...")
        
        # Esegue la scansione
        try:
            scanner.scan(target, ports=ports, arguments=arguments)
            self.print_scanned_port(scanner)
        except nmap.PortScannerError as e:
            print(f"Error during the scanning: {e}")

    def print_scanned_port(self, arg):
            # Stampa i risultati
            for host in arg.all_hosts():
                print_dynamic_dots('Host', host)
                print_dynamic_dots('State', arg[host].state())
                
                for proto in arg[host].all_protocols():
                    print_dynamic_dots('Protocol', proto)
                    ports = arg[host][proto].keys()
                    
                    for port in sorted(ports):
                        port_info = arg[host][proto][port]
                        print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info.get('version', 'N/A')}") 

    def port_blitz_manager(self):
        terminal_width = shutil.get_terminal_size().columns #terminal width
        print(f"\n{'='*40}{Fore.GREEN} PortBlitz{Style.RESET_ALL}{'='*40}")

        target = input("Enter IP or domain: ")
        ports = input("Enter ports to scan: ")
        arguments = input("Enter additional arguments (-sV, -A): ")

        self.nmap_port_scan(target, ports, arguments)
        print("=" * terminal_width + "\n")

