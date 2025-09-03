#!/home/rykerwilder/Documents/code/sentinel/sentinel-venv/bin/python3
from sentinel.utils import print_welcome_message
from simple_term_menu import TerminalMenu
from sentinel.modules import IPGlobeTracker, SystemInfo, NetworkScanner, PacketSniffer
from colorama import Fore, Style


def main():
    print_welcome_message()
    
    while True:
        options = [
            "[1] - Network scanner",
            "[2] - SystemInfo",
            "[3] - IP tracker",
            "[4] - Packet sniffer"
            "",
            "[x] Exit"
        ]
        
        terminal_menu = TerminalMenu(
            options,
            skip_empty_entries=True,
            menu_cursor="> ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("standout",)
        )
        
        choice = terminal_menu.show()
        
        # Gestione uscita con ESC o selezione "Exit"
        if choice is None or (choice == len(options) - 1):
            print(f'\n{Fore.BLUE}Thanks for using Sentinel, hope to see you soon!{Style.RESET_ALL}')
            break
        
        # Gestione scelte
        if choice == 0:
            print("PortScanner")
        elif choice == 1:
            SystemInfo().system_info_manager()
        elif choice == 2:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 3:
            network = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert network address to sniff ==> ")
            PacketSniffer().start_sniffing(network)
        elif choice == 4:
            pass
        elif choice == 5:
            pass

if __name__ == "__main__":
    main()