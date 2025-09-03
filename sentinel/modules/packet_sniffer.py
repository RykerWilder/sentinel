from scapy.all import sniff, IP, TCP, UDP, ICMP
from sentinel import write_to_result_file
import time
from colorama import Style, Fore

class PacketSniffer:
    def __init__(self):
        self.packet_count = 0
    
    def packet_callback(self, packet):
        if packet.haslayer(IP):
            self.packet_count += 1
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
            
            log_message = f"{ip_src} -> {ip_dst} | {protocol}"
            write_to_result_file(log_message)
            
    def start_sniffing(self, network, duration=30):
        try:
            ip_address = network.split('/')[0]
            
            start_msg = f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Sniffing started on {ip_address} for {duration} seconds."
            print(start_msg)
            write_to_result_file(start_msg)
            
            print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Sniffing in progress...")
            
            # Avvia lo sniffing con timeout
            sniff(prn=self.packet_callback, filter=f"host {ip_address}", store=0, timeout=duration)
            
            completion_msg = f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Sniffing completed, captured {self.packet_count} packets."
            print(completion_msg)
            write_to_result_file(completion_msg)
            
        except Exception as e:
            error_msg = f"{Fore.RED}[X] Sniffing error: {e}{Style.RESET_ALL}"
            print(error_msg)
            write_to_result_file(error_msg)