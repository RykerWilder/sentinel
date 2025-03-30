import requests
import shutil
from colorama import Style, Fore
from utils import print_dynamic_dots

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        terminal_width = shutil.get_terminal_size().columns #terminal width
        if data['status'] == 'success':
            print(f"\n{'='*40}{Fore.CYAN} IP Adress Info {Style.RESET_ALL}{'='*40}")
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
        else:
            print("Unable to get information for this IP")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user_ip = input('Insert IP Adress: ')
    get_ip_info(user_ip)