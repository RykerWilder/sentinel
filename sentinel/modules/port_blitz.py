import nmap
from colorama import Style, Fore
from sentinel import print_dynamic_dots
import shutil

class PortBlitz:
    def nmap_port_scan(self, target, ports, arguments):
        """
        Esegue una scansione delle porte con Nmap.
        
        Args:
            target (str): IP o dominio da scannerizzare (es. "192.168.1.1" o "scanme.nmap.org").
            ports (str): Range di porte (es. "1-1000", "22,80,443").
            arguments (str): Argomenti aggiuntivi per Nmap (es. "-sV" per version detection).
        """
        scanner = nmap.PortScanner()
        print(f"{Fore.YELLOW}Scanning \"{target}\" on ports {ports}")
        
        # Esegue la scansione
        try:
            scanner.scan(target, ports=ports, arguments=arguments)
            self.print_scanned_port(scanner)
        except nmap.PortScannerError as e:
            print(f"Error during the scanning: {e}")

    def print_scanned_port(self, arg):

        for host in arg.all_hosts():
            print_dynamic_dots('Host', host)
            print_dynamic_dots('State', arg[host].state())
            
            for proto in arg[host].all_protocols():
                print_dynamic_dots('Protocol', proto)
                ports = arg[host][proto].keys()
                
                for port in sorted(ports):
                    port_info = arg[host][proto][port]
                    state = port_info['state']
                    
                    # Determina il colore in base allo stato
                    if state == 'open':
                        state_color = Fore.GREEN
                    elif state == 'filtered':
                        state_color = Fore.YELLOW
                    elif state == 'closed':
                        state_color = Fore.RED
                    else:
                        state_color = Fore.WHITE  # default per altri stati
                    
                    print(f"{Fore.BLUE}Port{Style.RESET_ALL}: {port:<10}\t| "
                        f"{Fore.BLUE}State{Style.RESET_ALL}: {state_color}{state:<10}{Style.RESET_ALL}\t| "
                        f"{Fore.BLUE}Service{Style.RESET_ALL}: {port_info['name']:<20}\t| "
                        f"{Fore.BLUE}Version{Style.RESET_ALL}: {port_info.get('version', 'N/A')}")

    def port_blitz_manager(self):
        terminal_width = shutil.get_terminal_size().columns #terminal width
        print(f"\n{'='*40}{Fore.BLUE} PortBlitz{Style.RESET_ALL}{'='*40}")

        target = input("Enter IP or domain: ")
        ports = input("Enter ports to scan: ") or "1-1000"
        arguments = input("Enter additional arguments (-A, -oN scan.txt): ") or "-sV"

        self.nmap_port_scan(target, ports, arguments)
        print("=" * terminal_width + "\n")

