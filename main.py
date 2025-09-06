from sentinel.utils import print_welcome_message
from sentinel.modules import IPGlobeTracker, SystemInfo, NetworkScanner, PacketSniffer
from colorama import Fore, Style


def display_menu(options):
    """Display menu options with formatting"""
    
    for i, option in enumerate(options):
        if option.strip():  # Skip empty lines
            print(f"  {option}")
    

def get_user_choice(options):
    """Get user choice with input validation"""
    while True:
        try:
            choice = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert yout choice => ").strip().lower()
            
            if choice == 'x':
                return len(options) - 1  # Return exit option index
            
            if choice.isdigit():
                choice_num = int(choice)
                valid_options = [i for i, opt in enumerate(options) if opt.strip()]
                if 1 <= choice_num <= len(valid_options) - 1:
                    return valid_options[choice_num - 1]
            
            print(f"{Fore.RED}[ERROR] Invalid choice. Please try again.{Style.RESET_ALL}")
            
        except (ValueError, IndexError):
            print(f"{Fore.RED}[ERROR] Invalid input.{Style.RESET_ALL}")


def main():
    print_welcome_message()
    
    while True:
        options = [
            "[1] - Network scanner",
            "[2] - SystemInfo",
            "[3] - IP tracker",
            "[4] - Packet sniffer",
            "",
            "[ctrl + c] Exit"
        ]
        
        display_menu(options)
        choice = get_user_choice(options)
        
        
        # Gestione scelte
        if choice == 0:
            NetworkScanner().network_scanner_manager()
        elif choice == 1:
            SystemInfo().system_info_manager()
        elif choice == 2:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 3:
            PacketSniffer().start_sniffing()
        elif choice == 4:
            pass
        elif choice == 5:
            pass

if __name__ == "__main__":
    main()