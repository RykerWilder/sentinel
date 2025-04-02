from colorama import init, Fore
from sentinel import print_logo
from simple_term_menu import TerminalMenu
from sentinel.modules.ip_globetracker import IPGlobeTracker
import subprocess
init() # for windows
print(Fore.GREEN)

def main():
       while True:
              options = [
              "[1] PortBlitz",
              "[2] SysInsider",
              "[3] IP GlobeTracker",
              "[4] Network Sniffer",
              "[5] CVE Hunter",
              "[6] Exit"
              ]

              terminal_menu = TerminalMenu(
              options,
              menu_cursor=">",
              menu_cursor_style=("fg_red", "bold"),
              menu_highlight_style=("standout",)
              )

              choice = terminal_menu.show()
              if choice == 0:
                     print('scelta 1 - Scanner di porte')
              elif choice == 1:
                     subprocess.run(["python3", "sentinel/modules/sys_insider.py"])
              elif choice == 2:
                     ip_adress = input('Insert IP Adress: ')
                     globe_tracker = IPGlobeTracker()
                     globe_tracker.get_ip_info(ip_adress)
              elif choice == 3:
                     print('scelta 4 - Network sniffer')
              elif choice == 4:
                     subprocess.run(["python3", "sentinel/modules/cve_hunter.py"])
              if choice == 5: 
                     print('Thanks for using Sentinel, hope to see you soon!')
                     break

if __name__ == "__main__":
       print_logo()
       main()