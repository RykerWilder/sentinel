from colorama import Fore, Style
import subprocess
import sys
import shutil

class Holehe:
    def check_email(self, email):
        terminal_width = shutil.get_terminal_size().columns
        try:
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Checking: {email}")
            
            result = subprocess.run([
                'holehe', email, '--no-color'
            ], capture_output=True, text=False, timeout=120)
            
            if result.returncode == 0:
                # Decodifica bytes in stringa e poi split
                lines = result.stdout.decode('utf-8').split('\n')
                found_count = 0
                
                for line in lines:
                    if '[+]' in line or 'Found' in line:
                        found_count += 1
                        print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
                
                print(f"\n{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Found in {found_count} services")
            else:
                print(f"{Fore.RED}[X] Error running holehe{Style.RESET_ALL}")
                # Decodifica anche stderr
                print(result.stderr.decode('utf-8'))
                
        except FileNotFoundError:
            print(f"{Fore.RED}[X] Holehe not found. Install it with: pip install holehe{Style.RESET_ALL}")
        except subprocess.TimeoutExpired:
            print(f"{Fore.RED}[X] Operation timed out{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")
        
        print("=" * terminal_width + "\n")
    
    def holehe_manager(self):
        print(f"\n{'='*40}{Fore.MAGENTA} Holehe {Style.RESET_ALL}{'='*40}")
        email = input(f"\n{Fore.CYAN}┌─[Insert email to check] \n└──> {Style.RESET_ALL}").strip()
        
        if not email or "@" not in email:
            print(f"{Fore.RED}[X] Please insert a valid email{Style.RESET_ALL}")
            return
        
        self.check_email(email)