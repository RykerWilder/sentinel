import subprocess
import sys
import shutil
from colorama import Fore, Style

class Sherlock:
    def find(self, username, timeout):
        terminal_width = shutil.get_terminal_size().columns
        try:
            result = subprocess.run([
                'sherlock',  
                '--timeout', timeout,
                username
            ], capture_output=True, text=False, timeout=120)
            
            if result.returncode == 0:
                print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Research completed")
            else:
                print(f"{Fore.RED}[X] Error searching{Style.RESET_ALL}")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Timeout")
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")

        print("=" * terminal_width + "\n")

    def sherlock_manager(self):
        print(f"\n{'='*40}{Fore.MAGENTA} Sherlock {Style.RESET_ALL}{'='*40}")
        username = input(f"\n{Fore.CYAN}┌─[Insert username to search] \n└──> {Style.RESET_ALL}").strip()

        timeout = input(f"\n{Fore.CYAN}┌─[Insert timeout] \n└──> {Style.RESET_ALL}")

        if username:
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Searching: {username}")
            self.find(username, timeout)
        else:
            print(f"{Fore.RED}[X] Insert valid username{Style.RESET_ALL}")