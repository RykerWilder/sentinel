import requests
from requests.exceptions import RequestException
from datetime import datetime
import datetime as dt
from colorama import Style, Fore

class WebsiteCookie:
    def get_cookies(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Attempting connection to '{url}' to check cookies.")

        # init file content
        file_content = f"Cookies analysis for: {url}\n"
        file_content += f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

        try:
            response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
            response.raise_for_status() 

            if response.cookies:
                print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Cookies received from {response.url} (Status: {response.status_code})")
                
                # Aggiungi informazioni alla stringa del file
                file_content += f"Source URL: {response.url}\n"
                file_content += f"Status Code: {response.status_code}\n"
                file_content += f"Number of cookies found: {len(response.cookies)}\n\n"
                
                for cookie in response.cookies:
                    expires_str = "Session"
                    if cookie.expires:
                        try:
                            expires_str = datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S UTC')
                        except:
                            expires_str = str(cookie.expires)

                    # Aggiungi ogni cookie al contenuto del file
                    file_content += f"Name: {cookie.name}\n"
                    file_content += f"Value: {cookie.value}\n"
                    file_content += f"Domain: {cookie.domain}\n"
                    file_content += f"Path: {cookie.path}\n"
                    file_content += f"Secure: {cookie.secure}\n"
                    file_content += f"Expires: {expires_str}\n"
                    file_content += "-" * 20 + "\n\n"

                # Salva il contenuto nel file
                filename = self.write_to_result_file(file_content)
                if filename:
                    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Cookies saved to file: {filename}")
                else:
                    print(f"{Fore.RED}[X] Failed to save cookies to file {Style.RESET_ALL}")

            else:
                file_content += "No cookies found.\n"
                filename = self.write_to_result_file(file_content)
                if filename:
                    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Report saved to file: {filename} (no cookies found)")
                else:
                    print(f"{Fore.RED}[X] Failed to save report to file{Style.RESET_ALL}")

        except RequestException as e:
            error_msg = f"Network Error: Could not retrieve data/cookies.\nReason: {e}\n"
            print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
            #save errors in file
            file_content += f"ERROR: {error_msg}"
            self.write_to_result_file(file_content)
        except Exception as e:
            error_msg = f"An unexpected error occurred: {e}\n"
            print(f"{Fore.RED}[X] {error_msg}{Style.RESET_ALL}")
            #save errors in file
            file_content += f"ERROR: {error_msg}"
            self.write_to_result_file(file_content)

    def write_to_result_file(self, content):
        """
        create file result_DATE.txt and write into
        """
        # Ottieni la data corrente nel formato YYYYMMDD
        current_date = dt.datetime.now().strftime("%Y%m%d")
        filename = f"result_{current_date}.txt"
        
        try:
            # Scrivi il contenuto nel file (modalità append)
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(content + '\n' + '='*60 + '\n\n')
            return filename
        except Exception as e:
            print(f"{Fore.RED}[X] Error writing file: {e}{Style.RESET_ALL}")
            return None

    def get_website_cookies_manager(self):
        url = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Enter URL ==> ")

        if not url:
            print(f"{Fore.RED}[X] URL cannot be empty.{Style.RESET_ALL}")
            return
        
        self.get_cookies(url)

# Esempio di utilizzo
if __name__ == "__main__":
    cookie_checker = WebsiteCookie()
    cookie_checker.get_website_cookies_manager()