import requests
from colorama import init, Fore, Style
init(autoreset=True)

def check_cves_for_software(software_name):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={software_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica errori HTTP
        data = response.json()
        
        if data.get("totalResults", 0) > 0:
            print("\n" + "="*73 + " CVE Hunter " + "="*73)
            print(f"Found {Fore.RED}{data['totalResults']} CVE{Style.RESET_ALL} for {software_name}:")
            for vuln in data["vulnerabilities"]:
                cve_id = vuln["cve"]["id"]
                description = vuln["cve"]["descriptions"][0]["value"]
                print(f"{Fore.RED}{cve_id}{Style.RESET_ALL}: {description[:200]}...")
        else:
            print(f"No CVE found for {software_name}.")
    except Exception as e:
        print(f"Error while requesting: {e}")
    
    print("=" * 158 + "\n")

if __name__ == "__main__":
    user_software = input('Enter a software to analyze: ')
    check_cves_for_software(user_software)