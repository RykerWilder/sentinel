from colorama import init, Fore
from utils import print_logo, print_menu, select_choise

if __name__ == "__main__":
       init() # ANSI support for windows
       print(Fore.GREEN)
       print_logo()

       while True:
              user_choise = print_menu()
              
              if user_choise == 4:
                     print('Bye!')
                     break
              select_choise(user_choise)

