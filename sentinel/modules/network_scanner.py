from scapy.all import ARP, Ether, srp

class NetworkScanner:
    def arp_scan(self, ip_add):
        """
        Esegue una scansione ARP sulla rete specificata
        
        Args:
            ip_add (str): Indirizzo IP o range di IP da scansionare (es. "192.168.1.0/24")
        
        Returns:
            list: Lista di dizionari con IP e MAC address trovati
        """
        arp = ARP(pdst=ip_add)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []
        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        return clients

    def network_scanner_manager(self):
        """
        Gestisce l'interazione con l'utente per la scansione di rete
        """
        user_ip = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert IP to scan (es. 192.168.1.0/24) => ")
        clients = self.arp_scan(user_ip)
        
        print("\n" + "IP Address".ljust(16) + "    " + "MAC Address")
        print("-" * 40)
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))
        
        return clients