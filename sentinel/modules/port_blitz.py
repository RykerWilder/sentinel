import nmap

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
        print(f"Scanning {target} on ports {ports}...")
        
        # Esegue la scansione
        scanner.scan(target, ports=ports, arguments=arguments)
        self.print_scanned_port(scanner)
        
    def print_scanned_port(self, arg):
        # Stampa i risultati
        for host in arg.all_hosts():
            print(f"\nHost: {host} ({arg[host].hostname()})")
            print(f"State: {arg[host].state()}")
            
            for proto in arg[host].all_protocols():
                print(f"\nProtocol: {proto}")
                ports = arg[host][proto].keys()
                
                for port in sorted(ports):
                    port_info = arg[host][proto][port]
                    print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info.get('version', 'N/A')}")

