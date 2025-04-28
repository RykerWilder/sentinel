from colorama import Fore, Style
from sentinel.utils import print_logo
from simple_term_menu import TerminalMenu
from sentinel.modules import IPGlobeTracker, SysInsider, PortBlitz, MACPhantom

def main():
    print_logo()

    while True:
        options = [
            "[1] PortBlitz",
            "[2] SysInsider",
            "[3] IP GlobeTracker",
            "[4] PacketHound",
            "[5] MAC Phantom",
            "[6] CVE Hunter",
            "[esc] Exit"  # Aggiunta opzione esplicita per uscire
        ]

        terminal_menu = TerminalMenu(
            options,
            menu_cursor=">",
            menu_cursor_style=("fg_green", "bold"),
            menu_highlight_style=("standout",)
        )

        choice = terminal_menu.show()
        
        # Gestione uscita con ESC o selezione "Exit"
        if choice is None or (choice == len(options) - 1):
            print(f'\n{Fore.GREEN}Thanks for using Sentinel, hope to see you soon!{Style.RESET_ALL}')
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