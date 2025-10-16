from colorama import Style, Fore
import dns.resolver
from sentinel import write_to_result_file

class DNSInspector:
    def perform_dns_lookup(self, domain):
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME']
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Querying DNS records for {Fore.YELLOW}{domain}{Style.RESET_ALL}.")
        
        # HEADER
        header = f"DNS Lookup results for {domain}"

        for rtype in record_types:
            try:
                print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Querying {rtype} records.")
                answers = dns.resolver.resolve(domain, rtype)
                
                # WRITE RESULTS
                write_to_result_file(f"--- {rtype} Records ---")
                for rdata in answers:
                    write_to_result_file(f"  {rdata.to_text()}")

            except dns.resolver.NoAnswer:
                write_to_result_file(f"  No {rtype} records found.")
            except dns.resolver.NXDOMAIN:
                error_msg = f"Domain {domain} does not exist (NXDOMAIN)."
                write_to_result_file(error_msg)
                print(f"{Fore.RED}{error_msg}{Style.RESET_ALL}")
                return 
            except dns.resolver.Timeout:
                error_msg = f"DNS query timed out for {rtype} records."
                write_to_result_file(error_msg)
            except dns.resolver.NoNameservers:
                error_msg = f"Could not contact nameservers for {rtype} records."
                write_to_result_file(error_msg)
            except Exception as e:
                error_msg = f"Error querying {rtype} records: {e}"
                write_to_result_file(error_msg)
    
    def dns_inspector_manager(self):
        domain = input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert domain name ==> ")
        if not domain:
            print(f"{Fore.RED}[X] Domain name cannot be empty.{Style.RESET_ALL}")
            return
        
        self.perform_dns_lookup(domain)