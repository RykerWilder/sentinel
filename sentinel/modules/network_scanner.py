from scapy.all import ARP, Ether, srp, ICMP, IP, sr1, conf
import threading
import socket
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class NetworkScanner:
    def __init__(self):
        self.timeout = 2
        self.max_workers = 50  # max threads
        
    def arp_scan(self, ip_range):
        """
        Scansione ARP per rilevare dispositivi nella rete locale
        """
        try:
            arp = ARP(pdst=ip_range)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            result = srp(packet, timeout=self.timeout, verbose=0)[0]

            clients = []
            for sent, received in result:
                clients.append({
                    'ip': received.psrc, 
                    'mac': received.hwsrc,
                    'type': 'ARP'
                })
            return clients
        except Exception as e:
            print(f"{Fore.RED}[X]{Style.RESET_ALL} ARP scan error: {e}")
            return []

    def ping_sweep(self, ip_range):
        """
        Scansione ICMP (ping) per rilevare host attivi
        """
        network_prefix = '.'.join(ip_range.split('.')[:3])
        active_hosts = []
        
        def ping_host(ip):
            try:
                # Crea pacchetto ICMP
                packet = IP(dst=ip)/ICMP()
                response = sr1(packet, timeout=self.timeout, verbose=0)
                
                if response:
                    return {'ip': ip, 'type': 'ICMP'}
            except:
                pass
            return None
        
        # Scansione parallela degli host
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            
            # Per range come 192.168.1.0/24, scansiona da .1 a .254
            if '/24' in ip_range:
                for i in range(1, 255):
                    ip = f"{network_prefix}.{i}"
                    futures.append(executor.submit(ping_host, ip))
            else:
                # Per altri range, prova l'IP specificato
                futures.append(executor.submit(ping_host, ip_range.split('/')[0]))
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    active_hosts.append(result)
        
        return active_hosts

    def port_scan(self, ip, ports=[80, 443, 22, 21, 23, 53, 135, 139, 445, 3389]):
        open_ports = []
        
        def check_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                sock.close()
                if result == 0:
                    return port
            except:
                pass
            return None
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(check_port, port): port for port in ports}
            
            for future in as_completed(futures):
                port = future.result()
                if port:
                    open_ports.append(port)
        
        return open_ports

    def get_mac_vendor(self, mac_address):
        """
        Cerca il vendor del dispositivo basato sul MAC address
        """
        # Prima parte del MAC (OUI)
        oui = mac_address[:8].upper()
        
        # Database semplificato di vendor comuni
        vendors = {
            '00:14:22': 'Dell',
            '00:16:CB': 'Apple',
            '00:19:E3': 'D-Link',
            '00:1A:2B': 'Samsung',
            '00:1B:63': 'Microsoft',
            '00:1C:B3': 'Netgear',
            '00:1D:0F': 'Cisco',
            '00:1E:65': 'ASUS',
            '00:21:5A': 'Intel',
            '00:23:12': 'TP-Link',
            '00:24:01': 'Huawei',
            '00:26:5A': 'LG',
            '00:50:56': 'VMware',
            '08:00:27': 'VirtualBox',
            '08:18:1A': 'Sony',
            '0C:84:DC': 'Netgear',
            '10:9A:DD': 'Netgear',
            '14:CC:20': 'TP-Link',
            '18:A6:F7': 'TP-Link',
            '1C:1B:0D': 'Netgear',
            '20:4E:7F': 'Apple',
            '24:A2:E1': 'TP-Link',
            '28:16:AD': 'Netgear',
            '2C:30:33': 'ASUS',
            '30:5A:3A': 'ASUS',
            '34:23:BA': 'Apple',
            '3C:5A:B4': 'Google',
            '40:4D:7F': 'Samsung',
            '44:4E:1A': 'TP-Link',
            '48:5A:B6': 'Hon Hai',
            '4C:32:75': 'Apple',
            '54:60:09': 'ASUS',
            '60:03:08': 'Apple',
            '64:66:B3': 'Apple',
            '6C:94:F8': 'Apple',
            '70:3A:CB': 'Apple',
            '74:DA:38': 'TP-Link',
            '78:31:C1': 'Apple',
            '84:38:35': 'Apple',
            '88:53:95': 'Apple',
            '90:60:F1': 'Netgear',
            '94:0C:6D': 'TP-Link',
            'A4:4C:C8': 'Dell',
            'AC:BC:32': 'Apple',
            'B8:27:EB': 'Raspberry Pi',
            'BC:54:51': 'Netgear',
            'C0:25:A5': 'Dell',
            'C4:2C:03': 'Apple',
            'CC:46:D6': 'Cisco',
            'D0:57:85': 'TP-Link',
            'DC:A4:CA': 'Apple',
            'E4:CE:8F': 'Netgear',
            'EC:1A:59': 'Belkin',
            'F0:99:B6': 'Netgear',
            'F4:EC:38': 'TP-Link',
            'FC:A1:83': 'TP-Link'
        }
        
        return vendors.get(oui, 'Sconosciuto')

    def get_hostname(self, ip):
        """
        Prova a risolvere l'hostname dell'IP
        """
        try:
            hostname = socket.getfqdn(ip)
            if hostname != ip:
                return hostname
        except:
            pass
        return "N/D"

    def comprehensive_scan(self, ip_range):
        """
        Scansione completa che combina multiple tecniche
        """
        print(f"Scansione della rete {ip_range}...")
        
        # 1. Scansione ARP (più efficace in LAN)
        print("Eseguendo scansione ARP...")
        arp_results = self.arp_scan(ip_range)
        
        # 2. Scansione ICMP per host che non rispondono ad ARP
        print("Eseguendo ping sweep...")
        ping_results = self.ping_sweep(ip_range)
        
        # Combina i risultati
        all_ips = set()
        results = []
        
        # Aggiungi risultati ARP
        for device in arp_results:
            all_ips.add(device['ip'])
            # Scansione porte per dispositivi ARP
            open_ports = self.port_scan(device['ip'])
            device['ports'] = open_ports
            device['vendor'] = self.get_mac_vendor(device['mac'])
            device['hostname'] = self.get_hostname(device['ip'])
            results.append(device)
        
        # Aggiungi risultati ICMP non duplicati
        for device in ping_results:
            if device['ip'] not in all_ips:
                all_ips.add(device['ip'])
                open_ports = self.port_scan(device['ip'])
                hostname = self.get_hostname(device['ip'])
                results.append({
                    'ip': device['ip'],
                    'mac': 'N/D',
                    'type': 'ICMP',
                    'ports': open_ports,
                    'vendor': 'N/D',
                    'hostname': hostname
                })
        
        return results

    def network_scanner_manager(self):
        """
        Gestisce l'interazione con l'utente per la scansione di rete
        """
        print("=== SCANNER DI RETE AVANZATO ===")
        print("1. Scansione ARP (veloce)")
        print("2. Scansione completa (ARP + ICMP + Porte)")
        print("3. Solo ping sweep")
        
        choice = input("Scegli il tipo di scansione (1-3): ").strip()
        
        ip_range = input("Inserisci il range IP (es. 192.168.1.0/24): ").strip()
        
        start_time = time.time()
        
        if choice == '1':
            results = self.arp_scan(ip_range)
        elif choice == '2':
            results = self.comprehensive_scan(ip_range)
        elif choice == '3':
            results = self.ping_sweep(ip_range)
        else:
            print("Scelta non valida, uso scansione ARP")
            results = self.arp_scan(ip_range)
        
        end_time = time.time()
        
        # Visualizza risultati
        print(f"\nDispositivi trovati: {len(results)}")
        print(f"Tempo impiegato: {end_time - start_time:.2f} secondi")
        print("\n" + "IP Address".ljust(16) + "MAC Address".ljust(20) + "Vendor".ljust(25) + "Hostname".ljust(25) + "Porte Aperte")
        print("-" * 100)
        
        for device in results:
            ports_str = ', '.join(map(str, device.get('ports', []))) if device.get('ports') else 'Nessuna'
            print(f"{device['ip'].ljust(16)}{device.get('mac', 'N/D').ljust(20)}{device.get('vendor', 'N/D').ljust(25)}{device.get('hostname', 'N/D').ljust(25)}{ports_str}")
        
        return results