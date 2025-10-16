from colorama import Style, Fore
import dns.resolver
from sentinel import write_to_result_file

class DNSInspector:
    def perform_dns_lookup(self, domain):
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME']
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Querying DNS records for {Fore.YELLOW}{domain}{Style.RESET_ALL}.")
        
        #RESULTS LIST
        all_results = []
        all_results.append(f"DNS Lookup results for {domain}")
        all_results.append("=" * 50)

        for rtype in record_types:
            try:
                print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Querying {rtype} records.")
                answers = dns.resolver.resolve(domain, rtype)
                
                # Aggiungi i risultati alla lista
                all_results.append(f"--- {rtype} Records ---")
                for rdata in answers:
                    all_results.append(f"  {rdata.to_text()}")

            except dns.resolver.NoAnswer:
                all_results.append(f"  No {rtype} records found.")
            except dns.resolver.NXDOMAIN:
                error_msg = f"Domain {domain} does not exist (NXDOMAIN)."
                all_results.append(error_msg)
                print(f"{Fore.RED}{error_msg}{Style.RESET_ALL}")
                for result in all_results:
                    write_to_result_file(result)
                return 
            except dns.resolver.Timeout:
                error_msg = f"DNS query timed out for {rtype} records."
                all_results.append(error_msg)
            except dns.resolver.NoNameservers:
                error_msg = f"Could not contact nameservers for {rtype} records."
                all_results.append(error_msg)
            except Exception as e:
                error_msg = f"Error querying {rtype} records: {e}"
                all_results.append(error_msg)
        
        #WRITE ALL RESULTS
        for result in all_results:
            write_to_result_file(result)
    
    def dns_inspector_manager(self):
        domain = input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert domain name ==> ")
        if not domain:
            print(f"{Fore.RED}[X] Domain name cannot be empty.{Style.RESET_ALL}")
            return
        
        self.perform_dns_lookup(domain)