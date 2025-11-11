import sublist3r
from colorama import Fore, Style
import shutil
from sentinel import write_to_result_file

class Sublist3r:
    def find_domain(self, domain):
        terminal_width = shutil.get_terminal_size().columns
        try:
            subdomains = sublist3r.main(domain, 100, None, ports=None, silent=False, verbose=False, enable_bruteforce=False, engines=None)
            print(f"\n {Fore.MAGENTA}[INFO]{Style.RESET_ALL} Found {len(subdomains)} subdomains")
            for subdomain in subdomains:
                print(subdomain)
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")

        print("=" * terminal_width + "\n")

    def sublist3r_manager(self):
        print(f"\n{'='*40}{Fore.MAGENTA} Sublist3r {Style.RESET_ALL}{'='*40}")
        domain = input(f"\n{Fore.CYAN}┌─[Insert domain to check] \n└──> {Style.RESET_ALL}").strip()
        self.find_domain(domain)