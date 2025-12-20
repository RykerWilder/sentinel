from falcon.utils import print_welcome_message, exit
from falcon.modules import IPGlobeTracker, P2P, WebsiteCookie, WhoisDomainLookup, DNSInspector, Sherlock, Holehe, ExtractMetaData, PhoneNumberLookup
from colorama import Fore, Style
import signal

def main():
    print_welcome_message()

    #CTRL+C HANDLER
    signal.signal(signal.SIGINT, exit)
    
    while True:
        print(f"""
        [{Fore.CYAN}1{Style.RESET_ALL}] - Sherlock               [{Fore.CYAN}6{Style.RESET_ALL}] - Get websites cookies
        [{Fore.CYAN}2{Style.RESET_ALL}] - Phone Number Lookup    [{Fore.CYAN}7{Style.RESET_ALL}] - WHOIS Domain Lookup
        [{Fore.CYAN}3{Style.RESET_ALL}] - IP tracker             [{Fore.CYAN}8{Style.RESET_ALL}] - DNS Inspector
        [{Fore.CYAN}4{Style.RESET_ALL}] - Holehe                 [{Fore.CYAN}9{Style.RESET_ALL}] - Metadata Extractor
        [{Fore.CYAN}5{Style.RESET_ALL}] - Encrypted chat (P2P)   
        """)
        
        
        user_choice = input(f"\n{Fore.CYAN}┌─[Insert your choice] \n└──> {Style.RESET_ALL}")
        
        if not user_choice.strip():
            print(f"{Fore.RED}[X] Input cannot be empty.{Style.RESET_ALL}")
            continue
        else:
            choice = int(user_choice)

        
        
        #CHOICE MANAGEMENT
        if choice == 1:
            Sherlock().sherlock_manager()
        elif choice == 2:
            PhoneNumberLookup().phone_number_lookup_manager()
        elif choice == 3:
            IPGlobeTracker().ip_globetracker_manager()
        elif choice == 4:
            Holehe().holehe_manager()
        elif choice == 5:
            P2P().p2p_manager()
        elif choice == 6:
            WebsiteCookie().get_website_cookies_manager()
        elif choice == 7:
            WhoisDomainLookup().whois_lookup_manager()
        elif choice == 8:
            DNSInspector().dns_inspector_manager()
        elif choice == 9:
            ExtractMetaData().get_metadata_manager()
        else:
            pass

if __name__ == "__main__":
    main()