from colorama import Fore, init

def affianca_ascii_art(art1: str, art2: str, spacing: int = 4) -> str:
    """
    Affianca due ASCII art orizzontalmente con uno spazio personalizzabile.
    
    Args:
        art1 (str): Prima ASCII art.
        art2 (str): Seconda ASCII art.
        spacing (int): Spazio tra le due art (default: 4).
    
    Returns:
        str: Le due art affiancate come stringa multilinea.
    """
    lines1 = art1.split('\n')
    lines2 = art2.split('\n')
    
    # Trova la lunghezza massima tra le righe della prima art
    max_len1 = max(len(line) for line in lines1) if lines1 else 0
    
    # Allinea le righe mancanti con spazi vuoti (se le art hanno altezze diverse)
    max_lines = max(len(lines1), len(lines2))
    lines1 += [''] * (max_lines - len(lines1))
    lines2 += [''] * (max_lines - len(lines2))
    
    # Combina le righe affiancate
    combined = []
    for line1, line2 in zip(lines1, lines2):
        combined_line = f"{line1.ljust(max_len1)}{' ' * spacing}{line2}"
        combined.append(combined_line)
    
    return '\n'.join(combined)

# Esempio di utilizzo
if __name__ == "__main__":
    init(autoreset=True)  # Inizializza colorama
    
    # Prima ASCII art (esempio: un cuore)
    art1 = r"""
   _________              __  .__              .__                                                                                                     
 /   _____/ ____   _____/  |_|__| ____   ____ |  |       
 \_____  \_/ __ \ /    \   __\  |/    \_/ __ \|  |       
 /        \  ___/|   |  \  | |  |   |  \  ___/|  |__
/_______  /\___  >___|  /__| |__|___|  /\___  >____/
        \/     \/     \/             \/     \/    
    """
    
    # Seconda ASCII art (esempio: una stella)
    art2 = r"""
             )         
            (            
          '    }       
        (    '      
       '      (   
        )       ) 
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
         | | |
   /|    J_|_L    |\
   \ \___/ o \___/ /
    \_____ _ _____/
          |-|
          |-|
          |-|
         ,'-'.            
    """
    
    # Affianca le due art con uno spazio di 4 caratteri
    risultato = affianca_ascii_art(art1, art2)
    print(risultato)