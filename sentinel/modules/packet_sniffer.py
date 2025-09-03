from scapy.all import sniff, IP, TCP, UDP, ICMP
from sentinel import write_to_result_file

class PacketSniffer:
    def packet_callback(self, packet):
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = ""
            
            if packet.haslayer(TCP):
                protocol = f"TCP {packet[TCP].sport}->{packet[TCP].dport}"
            elif packet.haslayer(UDP):
                protocol = f"UDP {packet[UDP].sport}->{packet[UDP].dport}"
            elif packet.haslayer(ICMP):
                protocol = "ICMP"
            else:
                protocol = f"IP proto {packet[IP].proto}"
            
            # Crea il messaggio da loggare
            log_message = f"{ip_src} -> {ip_dst} | {protocol}"
            
            write_to_result_file(log_message)
            
    def start_sniffing(self, network):
        try:
            start_msg = f"[+] Sniffing started on {network}"
            write_to_result_file(start_msg)
            
            sniff(prn=self.packet_callback, filter=f"net {network}", store=0)
            
        except Exception as e:
            error_msg = f"[-] Sniffing error: {e}"
            write_to_result_file(error_msg)