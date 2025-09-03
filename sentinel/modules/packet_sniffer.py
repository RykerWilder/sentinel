from scapy.all import sniff, IP, TCP, UDP, ICMP

class PacketSniffer:
    def packet_callback(self, packet):
        # Verifica se è un pacchetto valido Scapy
        if hasattr(packet, 'show'):
            print(packet.show())
            print("-" * 50)
        else:
            print(f"Received: {packet}")
            
    def start_sniffing(self, network):
        try:
            print(f"[+] Starting packet sniffing on {network}")
            sniff(prn=self.packet_callback, filter="ip", store=0)
        except Exception as e:
            print(f"[-] Error in sniffing: {e}")