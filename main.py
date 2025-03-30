from colorama import init, Fore
from functions.utils import print_logo
from simple_term_menu import TerminalMenu
import subprocess
init() # for windows
print(Fore.CYAN)

def main():
       while True:
              options = [
              "[1] Port Scanner",
              "[2] System Info",
              "[3] IP Address Info",
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
                     subprocess.run(["python3", "functions/system_info.py"])
              elif choice == 2:
                     subprocess.run(["python3", "functions/ip_info.py"])
              elif choice == 3:
                     print('scelta 4 - Network sniffer')
              elif choice == 4:
                     subprocess.run(["python3", "functions/cve_hunter.py"])
              if choice == 5: 
                     print('Thanks for using Sentinel, hope to see you soon!')
                     break

if __name__ == "__main__":
       print_logo()
       main()