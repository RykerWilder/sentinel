import shutil
from colorama import Style, Fore, init

def clickable_link(url, text):
    return f"{Fore.YELLOW}\033]8;;{url}\033\\{text}\033]8;;\033\\{Style.RESET_ALL}"

def print_logo():
    logo = r"""
   _________              __  .__              .__           )      
 /   _____/ ____   _____/  |_|__| ____   ____ |  |          (       
 \_____  \_/ __ \ /    \   __\  |/    \_/ __ \|  |        '    }    
 /        \  ___/|   |  \  | |  |   |  \  ___/|  |__    (    '      
/_______  /\___  >___|  /__| |__|___|  /\___  >____/   '      (     
        \/     \/     \/             \/     \/          )  |    )   
                                                      '   /|\    `  
                                                     )   / | \  ` ) 
                                                    {    | | |  {   
                                                   }     | | |  .   
                                                    '    | | |    ) 
                                                   (    /| | |\    .
                                                    .  / | | | \  ( 
                                                  }    \ \ | / /  . 
                                                   (    \ `-' /    }
                                                   '    / ,-. \    '
                                                    }  / / | \ \  } 
                                                   '   \ | | | /   }
                                                    (   \| | |/  (  
                                                      )  | | |  )   
                                                      .  | | |  '   
                                                         J | L      
                                                   /|    J_|_L    |\
                                                   \ \___/ o \___/ /
                                                    \_____ _ _____/ 
                                                          |-|       
                                                          |-|       
                                                          |-|       
                                                         ,'-'.      
    """

    welcome_message = f"""{Fore.GREEN}Welcome to 
    {logo}
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