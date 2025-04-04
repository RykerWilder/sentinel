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
        
        # Stampa i risultati
        for host in scanner.all_hosts():
            print(f"\nHost: {host} ({scanner[host].hostname()})")
            print(f"State: {scanner[host].state()}")
            
            for proto in scanner[host].all_protocols():
                print(f"\nProtocol: {proto}")
                ports = scanner[host][proto].keys()
                
                for port in sorted(ports):
                    port_info = scanner[host][proto][port]
                    print(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info.get('version', 'N/A')}")

if __name__ == "__main__":
    target = input("Enter target (IP or domain): ")
    ports = input("Enter ports to scan (e.g. 1-1000, 22,80,443): ") or "1-1000"
    arguments = input("Enter additional arguments (e.g. -sV, -A): ") or "-sV"

    nmap_port_scan(target, ports, arguments)