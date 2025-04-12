import shutil
from colorama import Style, Fore

def clickable_link(url, text):
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def print_logo():
    logo = r"""
          ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░        
         ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
         ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
          ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░        
                ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
                ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
         ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░
    """

    welcome_message = f"""Welcome to 
    {logo}  
    If you want to learn more about sentinel's features, go read the documentation {clickable_link('https://github.com/RykerWilder/sentinel', 'sentinel documentation')}
    """

    return print(welcome_message)



def print_dynamic_dots(key, value):
    # Ottieni la larghezza corrente del terminale
    cols = shutil.get_terminal_size().columns
    
    #Calcola la lunghezza disponibile per i puntini
    available_space = cols - len(key) - len(str(value)) - 3  
    
    # Stampa la chiave, i puntini e il valore
    print(f"{Fore.BLUE}{key}{Style.RESET_ALL}: {'.' * available_space} {value}")