import requests
def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            print("\n" + "="*40 + " IP Adress info " + "="*40)
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Region: {data.get('regionName', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
            print(f"AS: {data.get('as', 'N/A')}")
            print("=" * 55 + "\n")
        else:
            print("Unable to get information for this IP")
    except Exception as e:
        print(f"Error: {e}")

# --- Main ---
if __name__ == "__main__": 
    user_ip = input('Inserisci l ip: ')
    get_ip_info(user_ip)