import shutil
from colorama import Style, Fore
import os
import datetime
import sys

def clickable_link(url, text):
    return f"{Fore.YELLOW}\033]8;;{url}\033\\{text}\033]8;;\033\\{Style.RESET_ALL}"

def print_welcome_message():
    logo = r"""
_________              __  .__              .__   
   _____/ ____   _____/  |_|__| ____   ____ |  |  
_____  \_/ __ \ /    \ / __\  |/    \_/ __ \|  |  
        \  ___/|   |  \\ | |  |   |  \  ___/|  |__
______  /\___  >___|  /__| |__|___|  /\___  >____/
      \/     \/     \//_           \/     \/                                 
"""
    welcome_message = f"""
{logo}

{Fore.YELLOW}[INFO]{Style.RESET_ALL} If you want to read more about Sentinel, go read {clickable_link('https://github.com/RykerWilder/sentinel', 'documentation')}.
"""
    print(welcome_message)

def print_dynamic_dots(key, value):
    # Ottieni la larghezza corrente del terminale
    cols = shutil.get_terminal_size().columns
    
    #Calcola la lunghezza disponibile per i puntini
    available_space = cols - len(key) - len(str(value)) - 3  
    
    # Stampa la chiave, i puntini e il valore
    print(f"{Fore.BLUE}{key}{Style.RESET_ALL}: {'.' * available_space} {value}")

def write_to_result_file(content):
    """
    Crea un file result_DATE.txt e scrive il contenuto
    """
    # Ottieni la data corrente nel formato YYYYMMDD
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"result{current_date}.txt"
    
    try:
        # Scrivi il contenuto nel file (modalità append)
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content + '\n')
        return filename
    except Exception as e:
        print(f"{Fore.RED}[X] Error writing file: {e}{Style.RESET_ALL}")
        return None

def exit(signum, frame):
    print(f"\n{Fore.YELLOW}[INFO]{Style.RESET_ALL} Sentinel shutdown, thanks to using sentinel.")
    sys.exit(0)