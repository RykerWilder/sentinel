from colorama import Fore, Style
from sentinel.utils import print_logo
from simple_term_menu import TerminalMenu
from sentinel.modules import IPGlobeTracker, SysInsider, PortBlitz, KeyboardHandler
from pynput import keyboard
print(Fore.GREEN)

def main():
       keyboard_handler = KeyboardHandler()
       # Avvia il listener
       listener = keyboard.Listener(on_press=keyboard_handler.on_press_exit)
       listener.start()

       print_logo()

       while not keyboard_handler.should_exit:
              options = [
              "[1] PortBlitz",
              "[2] SysInsider",
              "[3] IP GlobeTracker",
              "[4] PacketHound",
              "[5] MAC Phantom",
              "[6] CVE Hunter"
              ]

              terminal_menu = TerminalMenu(
              options,
              menu_cursor=">",
              menu_cursor_style=("fg_green", "bold"),
              menu_highlight_style=("standout",)
              )

              choice = terminal_menu.show()
              
              if choice == 0:
                     port_blitz = PortBlitz()
                     port_blitz.port_blitz_manager()
              elif choice == 1:
                     sys_insider = SysInsider() 
                     sys_insider.print_system_info()
              elif choice == 2:
                     globe_tracker = IPGlobeTracker()
                     globe_tracker.ip_globetracker_manager()
              elif choice == 3:
                     print('scelta 4 - PacketHound')
              elif choice == 4:
                     print('scelta 5 - MAC Phantom')
              

       listener.stop()  # Ferma correttamente il listener
       print(f'{Fore.GREEN}Thanks for using Sentinel, hope to see you soon!{Style.RESET_ALL}')

if __name__ == "__main__":
       main()