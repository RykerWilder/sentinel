import subprocess
import argparse
import re
import random

class MACPhantom:
    def get_current_mac(self ,interface):
        try:
            result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.DEVNULL)
            mac_address = re.search(r"ether\s(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})", result.decode())
            return mac_address.group(1) if mac_address else None
        except:
            return None

    def change_mac(self, interface, new_mac):
        print(f"[*] Changing MAC address for {interface} to {new_mac}")
        
        # Disable the interface
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        
        # Change the MAC address
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        
        # Enable the interface
        subprocess.call(["sudo", "ifconfig", interface, "up"])

    def generate_random_mac(self):
        # Generate a valid MAC address (second byte must be even)
        mac = [ 0x00, 
                random.randint(0x00, 0xff) & 0xfe,  # second byte must be even
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff) ]
        
        return ':'.join(map(lambda x: "%02x" % x, mac))

    def mac_phantom_manager(self):
        parser = argparse.ArgumentParser(description="Python MAC Address Spoofer")
        parser.add_argument("-i", "--interface", help="Network interface name")
        parser.add_argument("-m", "--mac", help="New MAC address (leave empty to generate random)")
        args = parser.parse_args()

        if not args.interface:
            print("[-] Please specify a network interface. Use --help for more information.")
            return
        
        current_mac = self.get_current_mac(args.interface)
        print(f"[*] Current MAC address for {args.interface}: {current_mac}")
        
        new_mac = args.mac if args.mac else self.generate_random_mac()
        
        self.change_mac(args.interface, new_mac)
        
        current_mac = self.get_current_mac(args.interface)
        if current_mac == new_mac:
            print(f"[+] MAC address successfully changed to {current_mac}")
        else:
            print("[-] Failed to change MAC address")