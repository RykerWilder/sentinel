from simple_term_menu import TerminalMenu
from colorama import init, Fore
import subprocess

init() # ANSI support for windows
print(Fore.GREEN)

def print_logo():
    print(""" 
    ___________________________________________________________________________
    |     ______         _                 _    _  _  _      _                 |
    |     | ___ \       | |               | |  | |(_)| |    | |                | 
    |     | |_/ / _   _ | | __  ___  _ __ | |  | | _ | |  __| |  ___  _ __     |
    |     |    / | | | || |/ / / _ \| '__|| |/\| || || | / _` | / _ \| '__|    |
    |     | |\ \ | |_| ||   < |  __/| |   \  /\  /| || || (_| ||  __/| |       |
    |     \_| \_| \__, ||_|\_\ \___||_|    \/  \/ |_||_| \__,_| \___||_|       |
    |              __/ |                                                       |
    |             |___/                                                        |
    |__________________________________________________________________________|
    |                                                                          |
    |      ███▄ ▄███▓ ▒█████   ██▓     ▒█████  ▄▄▄█████▓ ▒█████   ██▒   █▓     |
    |     ▓██▒▀█▀ ██▒▒██▒  ██▒▓██▒    ▒██▒  ██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░   █▒     |
    |     ▓██    ▓██░▒██░  ██▒▒██░    ▒██░  ██▒▒ ▓██░ ▒░▒██░  ██▒ ▓██  █▒░     |
    |     ▒██    ▒██ ▒██   ██░▒██░    ▒██   ██░░ ▓██▓ ░ ▒██   ██░  ▒██ █░░     |
    |     ▒██▒   ░██▒░ ████▓▒░░██████▒░ ████▓▒░  ▒██▒ ░ ░ ████▓▒░   ▒▀█░       |
    |     ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░   ▒ ░░   ░ ▒░▒░▒░    ░ ▐░       |
    |     ░  ░      ░  ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░     ░      ░ ▒ ▒░    ░ ░░       |
    |     ░      ░   ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒    ░      ░ ░ ░ ▒       ░░       |
    |           ░       ░ ░      ░  ░    ░ ░               ░ ░        ░        |
    |                                                             ░            |
    |__________________________________________________________________________|                                               
    """)

def print_menu():
    options = [
        "[1] Port Scanner",
        "[2] System Info",
        "[3] IP Info",
        "[4] Network sniffer",
        "[5] Exit"
    ]
    
    terminal_menu = TerminalMenu(
        options,
        menu_cursor="❯ ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("standout",)
    )
    
    choice_index = terminal_menu.show()
    
    return choice_index

def select_choise(choise):
    if choise == 0:
        print('scelta 1 - Scanner di porte')
    elif choise == 1:
        subprocess.run(["python3", "functions/system_info.py"])
    elif choise == 2:
        subprocess.run(["python3", "functions/ip_info.py"])
    elif choise == 3:
        print('scelta 4 - Network sniffer')