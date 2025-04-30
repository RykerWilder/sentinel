import shutil
from colorama import Style, Fore

def clickable_link(url, text):
    return f"{Fore.YELLOW}\033]8;;{url}\033\\{text}\033]8;;\033\\{Style.RESET_ALL}"

def print_welcome_message():
    logo = r"""
                                        _________              __  .__              .__       
                   _.--.    .--._          _____/ ____   _____/  |_|__| ____   ____ |  |  
                 ."  ."      ".  ".     _____  \_/ __ \ /    \ / __\  |/    \_/ __ \|  |  
                ;  ."    /\    ".  ;            \  ___/|   |  \\ | |  |   |  \  ___/|  |__
                ;  '._,-/  \-,_.`  ;    ______  /\___  >___|  /__| |__|___|  /\___  >____/
                \  ,`  / /\ \  `,  /          \/     \/     \//_           \/     \/      
                 \/    \/  \/    \/                                                       
                 ,=_    \/\/    _=,                                                       
                 |xx"_   \/   _"xx|                                                       
                 |xxxxx"-..-"xxxxx|                       | By        : RykerWilder                               
                 | "-.xxxxxxxxx-" |                       | Version   : 0.1.0                               
                 |    "\xxxx/"    |                                                       
                 |      |xx|      |                                                       
         ___     |      |xx|      |     ___                                               
     _,-",  ",   '_     |xx|     _'   ,"  ,"-,_                                           
   _(  \  \   \"=--"-.  |xx|  .-"--="/   /  /  )_                                         
 ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".                                       
!     \  \  \   \                  /   /  /  /     !                                      
|      \  \  \   \                /   /  /  /      |                                                                        
"""
    logo_colored = logo.replace("RykerWilder", f"{Fore.BLUE}RykerWilder{Style.RESET_ALL}{Fore.RED}") \
                      .replace("0.1.0", f"{Fore.BLUE}0.1.0{Style.RESET_ALL}{Fore.RED}")

    welcome_message = f"""{Fore.RED}{logo_colored}
    If you want to learn more about Sentinel, go read {clickable_link('https://github.com/RykerWilder/sentinel', 'sentinel documentation')}{Fore.GREEN}.
    """

    return print(welcome_message)



def print_dynamic_dots(key, value):
    # Ottieni la larghezza corrente del terminale
    cols = shutil.get_terminal_size().columns
    
    #Calcola la lunghezza disponibile per i puntini
    available_space = cols - len(key) - len(str(value)) - 3  
    
    # Stampa la chiave, i puntini e il valore
    print(f"{Fore.BLUE}{key}{Style.RESET_ALL}: {'.' * available_space} {value}")