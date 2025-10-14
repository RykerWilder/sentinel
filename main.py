from sentinel.utils import print_welcome_message, exit
from sentinel.modules import IPGlobeTracker, SystemInfo, NetworkScanner, PacketSniffer, P2P, WebsiteCookie
from colorama import Fore, Style
import signal

def main():
    print_welcome_message()

    #CTRL+C HANDLER
    signal.signal(signal.SIGINT, exit)
    
    while True:
        print(f"""
            [{Fore.BLUE}1{Style.RESET_ALL}] - Network scanner
            [{Fore.BLUE}2{Style.RESET_ALL}] - System info
            [{Fore.BLUE}3{Style.RESET_ALL}] - IP tracker
            [{Fore.BLUE}4{Style.RESET_ALL}] - Packet sniffer
            [{Fore.BLUE}5{Style.RESET_ALL}] - Encrypted chat (P2P)
            [{Fore.BLUE}6{Style.RESET_ALL}] - Get websites cookies
        """)
        
        
        try:
            choice = int(input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert your choice => "))
        except (ValueError, IndexError):
            print(f"{Fore.RED}[ERROR] Invalid input.{Style.RESET_ALL}")

        
        
        #CHOICE MANAGEMENT
        if choice == 1:
            NetworkScanner().network_scanner_manager()
        elif choice == 2:
            SystemInfo().system_info_manager()
        elif choice == 3:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 4:
            PacketSniffer().start_sniffing()
        elif choice == 5:
            P2P().p2p_manager()
        elif choice == 6:
            WebsiteCookie().get_website_cookies_manager()
        elif choice == 6:
            pass

if __name__ == "__main__":
    main()