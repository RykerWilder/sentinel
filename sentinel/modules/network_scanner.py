from scapy.all import ARP, Ether, srp

class NetworkScanner:
    def arp_scan(ip_range):
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []
        for sent, received in result:
            clients.append({'ip': received.psrc,'mac': received.hwsrc})
        return clients

    ip_range = "192.168.1.0/24"
    clients = arp_scan(ip_range)
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))