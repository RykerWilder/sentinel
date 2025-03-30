import requests
import shutil
from colorama import Fore, Style

def check_cves_for_software(software_name):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={software_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica errori HTTP
        data = response.json()
        terminal_width = shutil.get_terminal_size().columns #terminal width

        if data.get("totalResults", 0) > 0:
            print(f"\n{'='*40}{Fore.CYAN} CVE Hunter {Style.RESET_ALL}{'='*40}")
            print(f"Found {Fore.RED}{data['totalResults']} CVE{Style.RESET_ALL} for {software_name}:")
            for vuln in data["vulnerabilities"]:
                cve_id = vuln["cve"]["id"]
                description = vuln["cve"]["descriptions"][0]["value"]
                print(f"{Fore.RED}{cve_id}{Style.RESET_ALL}: {description[:200]}...")
        else:
            print(f"No CVE found for {software_name}.")
    except Exception as e:
        print(f"Error while requesting: {e}")
    
    print("=" * terminal_width + "\n")

if __name__ == "__main__":
    user_software = input('Enter a software to analyze: ')
    check_cves_for_software(user_software)