import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

class Sherlock:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    def find(self, username, timeout):
        try:
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Sherlock starting search for: {username}")
            
            result = subprocess.run([
                'sherlock', 
                '--timeout', timeout, 
                '--output', './data/' + username + '.txt',
                username
            ], capture_output=True, text=False, timeout=120)
            
            if result.returncode == 0:
                print(f"{Fore.MAGENTA}\n [INFO] Sherlock has finished searching for the username: {username}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[X] Error searching {username}{Style.RESET_ALL}")
                print(result.stderr)
                
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[X] Timeout for {username}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[X] Error for {username}: {e}{Style.RESET_ALL}")

    def sherlock_manager(self):
        print(f"\n{'='*40}{Fore.MAGENTA} Sherlock {Style.RESET_ALL}{'='*40}")
        username = input(f"\n{Fore.CYAN}┌─[Insert username to search] \n└──> {Style.RESET_ALL}").strip()
                
        if username:
            timeout = input(f"{Fore.CYAN}┌─[Insert timeout (press Enter for default)] \n└──> {Style.RESET_ALL}").strip()
            if not timeout:
                timeout = "10" 
                
        #START IN SPLIT THREAD
            self.executor.submit(self.find, username, timeout)
        else:
            print(f"{Fore.RED}[X] Insert valid username{Style.RESET_ALL}")