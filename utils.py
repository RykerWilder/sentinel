from simple_term_menu import TerminalMenu

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
        "[1] Scanner di porte",
        "[2] Analisi vulnerabilità",
        "[3] Password cracking",
        "[4] Network sniffer",
        "[5] Esci"
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
        print('scelta 2 - Analisi vulnerabilità')
    elif choise == 2:
        print('scelta 3 - Password cracking')
    elif choise == 3:
        print('scelta 4 - Network sniffer')