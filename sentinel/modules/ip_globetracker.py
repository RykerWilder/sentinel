import requests
import shutil
from colorama import Style, Fore
from sentinel import print_dynamic_dots
from sentinel.modules.system_info import SystemInfo
class IPGlobeTracker(SystemInfo):

    def get_ip_info(self, ip_address):
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_address}")
            data = response.json()
            if data['status'] == 'success':
                self.print_ip_info(data)
            else:
                print(f"{Fore.RED}[X] Unable to get information for this IP.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")

    def print_ip_info(self, data):
        terminal_width = shutil.get_terminal_size().columns #terminal width
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Your public IP address is: {data.get('query')}")
        print_dynamic_dots('Country', data.get('country'))
        print_dynamic_dots('Country code', data.get('countryCode'))
        print_dynamic_dots('Region', data.get('regionName'))
        print_dynamic_dots('City', data.get('city'))
        print_dynamic_dots('Latitude', data.get('lat'))
        print_dynamic_dots('Longitude', data.get('lon'))
        print_dynamic_dots('Timezone', data.get('timezone'))
        print_dynamic_dots('ISP', data.get('isp'))
        print_dynamic_dots('Organization', data.get('org'))
        print_dynamic_dots('AS', data.get('as'))
        print("=" * terminal_width + "\n")

    def ip_globetracker_manager(self):
        print(f"\n{'='*40}{Fore.BLUE} IP GlobeTracker {Style.RESET_ALL}{'='*40}")
        print(f""" 
            [{Fore.BLUE}1{Style.RESET_ALL}] Check my public IP
            [{Fore.BLUE}2{Style.RESET_ALL}] Check a specific IP/domain
        """)

        try:
            choice = int(input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert yout choice => "))
        except (ValueError, IndexError):
            print(f"{Fore.RED}[X] Input cannot be empty.{Style.RESET_ALL}")
            return
            
        if choice == 1:
            my_ip_address = self.get_public_ip()
            self.get_ip_info(my_ip_address)
        if choice == 2:
            ip_address = input(f"{Fore.BLUE}[?]{Style.RESET_ALL} Insert IP address or domain ==> ")
            self.get_ip_info(ip_address)