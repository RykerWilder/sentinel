import whois
from colorama import Fore, Style
from sentinel import write_to_result_file

class WhoisDomainLookup:
    def whois_lookup(self, domain):
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Querying WHOIS for {Fore.CYAN}{domain}{Style.RESET_ALL}.")
        try:
            w = whois.whois(domain)
            
            if w.status is None and not w.domain_name: 
                error_msg = f"Could not retrieve WHOIS data for {domain}. Domain might not exist or WHOIS server unavailable."
                print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
                write_to_result_file(error_msg)
                
            #WRITE RESULT INTO FILE
            success_msg = f"--- WHOIS Information for {domain} ---"
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} WHOIS data retrieved successfully. Writing to file...")
            write_to_result_file(success_msg)
            
            for key, value in w.items():
                if key != 'text' and value:
                    if isinstance(value, list):
                        line = f"{key.replace('_', ' ').title():<25}: {', '.join(map(str, value))}"
                    else:
                        line = f"{key.replace('_', ' ').title():<25}: {value}"
                    write_to_result_file(line)
                    
        except Exception as e:
            error_msg = f"An unexpected error occurred during WHOIS lookup for {domain}: {str(e)}"
            print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
            write_to_result_file(error_msg)

    def whois_lookup_manager(self):
        domain = input(f"\n{Fore.CYAN}┌─[Insert domain name] \n└──> {Style.RESET_ALL}")
        if not domain:
            print(f"{Fore.RED}[X] Domain name cannot be empty.{Style.RESET_ALL}")
            return
                
        self.whois_lookup(domain)