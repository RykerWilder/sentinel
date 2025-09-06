from scapy.all import ARP, Ether, srp

class NetworkScanner:
    def arp_scan(self, ip_add):
        arp = ARP(pdst=ip_add)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []
        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        return clients

    def network_scanner_manager():
        user_ip = input("Insert IP to scan => ")
        self.arp_scan(user_ip)

# Utilizzo della classe
if __name__ == "__main__":
    
    print("IP Address".ljust(16) + "    " + "MAC Address")
    print("-" * 40)
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))