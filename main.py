from colorama import Fore, Style
from sentinel.utils import print_welcome_message
from simple_term_menu import TerminalMenu
from sentinel.modules import IPGlobeTracker, SysInsider, PortBlitz, MACPhantom

def main():
    print_welcome_message()

    while True:
        options = [
            "[1] PortBlitz",
            "[2] SysInsider",
            "[3] IP GlobeTracker",
            "[4] PacketHound",
            "[5] MAC Phantom",
            "[6] CVE Hunter",
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
            PortBlitz().port_blitz_manager()
        elif choice == 1:
            SysInsider().print_system_info()
        elif choice == 2:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 3:
            print('PacketHound (funzionalità non implementata)')
        elif choice == 4:
            MACPhantom().mac_phantom_manager()
        elif choice == 5:
            print('CVE Hunter (funzionalità non implementata)')

if __name__ == "__main__":
    main()