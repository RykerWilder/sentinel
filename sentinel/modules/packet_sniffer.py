from scapy.all import sniff

class PacketSniffer:
    def packet_callback(packet):
        print(packet.show())

    sniff(prn=packet_callback)