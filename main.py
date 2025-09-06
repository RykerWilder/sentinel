from sentinel.utils import print_welcome_message, exit
from sentinel.modules import IPGlobeTracker, SystemInfo, NetworkScanner, PacketSniffer
from colorama import Fore, Style
import signal

def main():
    print_welcome_message()

    # ctrl+c handler
    signal.signal(signal.SIGINT, exit)
    
    while True:
        print(f"""
            [{Fore.BLUE}1{Style.RESET_ALL}] - Network scanner
            [{Fore.BLUE}2{Style.RESET_ALL}] - SystemInfo
            [{Fore.BLUE}3{Style.RESET_ALL}] - IP tracker
            [{Fore.BLUE}4{Style.RESET_ALL}] - Packet sniffer
        """)
        
        
        try:
            choice = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert yout choice => ")
        except (ValueError, IndexError):
            print(f"{Fore.RED}[ERROR] Invalid input.{Style.RESET_ALL}")

        
        
        # Gestione scelte
        if choice == 1:
            NetworkScanner().network_scanner_manager()
        elif choice == 2:
            SystemInfo().system_info_manager()
        elif choice == 3:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 4:
            PacketSniffer().start_sniffing()
        elif choice == 5:
            pass
        elif choice == 6:
            pass

if __name__ == "__main__":
    main()