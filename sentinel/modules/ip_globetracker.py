import requests
import shutil
from simple_term_menu import TerminalMenu
from colorama import Style, Fore
from sentinel import print_dynamic_dots
from sentinel.modules.system_info import SystemInfo
class IPGlobeTracker(SystemInfo):

    def get_ip_info(self, ip_address):
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_address}")
            data = response.json()
            if data['status'] == 'success':
                self.print_ip_info(data);
            else:
                print(f"{Fore.RED}Unable to get information for this IP{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

    def print_ip_info(self, data):
        terminal_width = shutil.get_terminal_size().columns #terminal width
        print(f'Your public IP address is: {Fore.YELLOW}{data.get('query')}{Style.RESET_ALL}')
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
        options = [
            "[1] Check my public IP",
            "[2] Check a specific IP/domain"
        ]

        terminal_menu = TerminalMenu(
            options,
            menu_cursor=">",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("standout",)
        )

        choice = terminal_menu.show()
        
        if choice == 0:
            my_ip_address = self.get_public_ip()
            self.get_ip_info(my_ip_address)
        if choice == 1:
            ip_address = input('Insert IP address or domain ==> ')
            self.get_ip_info(ip_address)