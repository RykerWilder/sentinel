import requests
import shutil
from colorama import Style, Fore
from sentinel import print_dynamic_dots

class IPGlobeTracker:

    def get_ip_info(self, ip_address):
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_address}")
            data = response.json()
            if data['status'] == 'success':
                self.print_ip_info(data);
            else:
                print("Unable to get information for this IP")
        except Exception as e:
            print(f"Error: {e}")

    def print_ip_info(self, data):
        terminal_width = shutil.get_terminal_size().columns #terminal width
        print(f"\n{'='*40}{Fore.GREEN} IP GlobeTracker {Style.RESET_ALL}{'='*40}")
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