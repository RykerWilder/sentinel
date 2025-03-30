import requests

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            print("\n" + "="*40 + " IP Adress info " + "="*40)
            print(f"Country: {data.get('country')}")
            print(f"Country code: {data.get('countryCode')}")
            print(f"Region: {data.get('regionName')}")
            print(f"City: {data.get('city')}")
            print(f"Latitude: {data.get('lat')}")
            print(f"Longitude: {data.get('lon')}")
            print(f"Timezone: {data.get('timezone')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Organization: {data.get('org')}")
            print(f"AS: {data.get('as')}")
            print("=" * 55 + "\n")
        else:
            print("Unable to get information for this IP")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__": 
    user_ip = input('Insert IP Adress: ')
    get_ip_info(user_ip)