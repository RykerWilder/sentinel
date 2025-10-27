import subprocess
import sys
from colorama import Fore, Style

class Sherlock:
    def find(self, username, timeout):
        try:
            result = subprocess.run([
                'sherlock',  
                '--timeout', timeout,
                username
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Research completed")
                print(result.stdout)
            else:
                print(f"{Fore.RED}[X] Error searching{Style.RESET_ALL}")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Timeout")
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")

    def sherlock_manager(self):
        username = input(f"\n{Fore.CYAN}┌─[Insert username to search] \n└──> {Style.RESET_ALL}").strip()

        timeout = input(f"\n{Fore.CYAN}┌─[Insert timeout] \n└──> {Style.RESET_ALL}")

        if username:
            self.find(username, timeout)
        else:
            print(f"{Fore.RED}[X] Insert valid username{Style.RESET_ALL}")