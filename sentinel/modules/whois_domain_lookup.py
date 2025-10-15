import whois
from colorama import Fore, Style
import datetime
import os

class WhoisDomainLookup:
    def whois_lookup(self, domain):
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Querying WHOIS for {Fore.YELLOW}{domain}{Style.RESET_ALL}.")
        try:
            w = whois.whois(domain)
            if w.status is None and not w.domain_name: 
                error_msg = f"Could not retrieve WHOIS data for {domain}. Domain might not exist or WHOIS server unavailable."
                print(f"{Fore.RED}[X]{Style.RESET_ALL} {error_msg}")
                self.write_to_result_file(error_msg)
                if hasattr(w, 'text'): 
                    raw_snippet = f"Raw Response Snippet:\n{w.text[:500]}..."
                    self.write_to_result_file(raw_snippet)
            else:
                success_msg = f"--- WHOIS Information for {domain} ---"
                print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} WHOIS data retrieved successfully. Writing to file...")
                self.write_to_result_file(success_msg)
                
                for key, value in w.items():
                    if key != 'text' and value:
                        if isinstance(value, list):
                            line = f"{key.replace('_', ' ').title():<20}: {', '.join(map(str, value))}"
                        else:
                            line = f"{key.replace('_', ' ').title():<20}: {value}"
                        self.write_to_result_file(line)
                
        except whois.parser.PywhoisError as e:
            error_msg = f"WHOIS Error for {domain}: {e}"
            print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
            self.write_to_result_file(error_msg)
        except Exception as e:
            error_msg = f"An unexpected error occurred during WHOIS lookup for {domain}: {e}"
            print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
            self.write_to_result_file(error_msg)

    def whois_lookup_manager(self):
        try:
            domain = input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Enter domain name ==> ")
            if not domain.strip():
                print(f"{Fore.RED}[X] Domain name cannot be empty.{Style.RESET_ALL}")
                return
        except (ValueError, IndexError):
            print(f"{Fore.RED}[X] Input cannot be empty.{Style.RESET_ALL}")
            return
        
        self.whois_lookup(domain)

    def write_to_result_file(self, content):
        """
        Create file result_DATE.txt in data folder and write into it
        """
        current_date = datetime.datetime.now().strftime("%Y%m%d")
        data_folder = "./data"
        
        #CREATE FOLDER IF NOT EXISTS
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        
        #PATH
        filename = os.path.join(data_folder, f"result_{current_date}.txt")
        
        try:
            #WRITE CONTENT
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {content}\n")
            return filename
        except Exception as e:
            print(f"{Fore.RED}[X] Error writing file: {e}{Style.RESET_ALL}")
            return None