import socket
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Style, Fore

class NetworkScanner:
    def __init__(self, threads=50):
        self.threads = threads
        self.common_ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 993, 995, 3389, 5900, 8080]
    
    def _scan_host(self, ip):
        """scanning a single host for open service"""
        open_ports = []
        
        for port in self.common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((str(ip), port))
                sock.close()
                
                if result == 0:
                    open_ports.append(port)
            except:
                pass
        
        if open_ports:
            print(f"{ip}: {open_ports}")
        
        return len(open_ports) > 0
    
    def network_scanner_manager(self):
        """scan network and print open services"""

        try:
            network = input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert network address to scan ==> ")
        except (ValueError, IndexError):
            print(f"{Fore.RED}[X] URL cannot be empty.{Style.RESET_ALL}")
            return

        try:
            net = ipaddress.IPv4Network(network, strict=False)
        except ValueError:
            print(f"{Fore.RED}[X] Error: Network invalid.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Scanning network {Fore.YELLOW}{network}{Style.RESET_ALL}...")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(self._scan_host, ip) for ip in net.hosts()]
            
            # Attendi completamento
            active_hosts = sum(1 for future in futures if future.result())
        
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL}Scan completed. Active hosts {active_hosts}.")