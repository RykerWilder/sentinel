import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class SQLInjectionScanner:
    def __init__(self, timeout=10):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        self.timeout = timeout
        self.vulnerable_errors = {
            "quoted string not properly terminated",
            "unclosed quotation mark",
            "sql syntax error",
            "syntax error near"
        }

    def get_forms(self, url):
        try:
            response = self.session.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.find_all("form")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error fetching {url}: {e}")
            return []

    @staticmethod
    def get_form_details(form):
        details = {
            "action": form.attrs.get("action", "").lower(),
            "method": form.attrs.get("method", "get").lower(),
            "inputs": []
        }
        for input_tag in form.find_all("input"):
            details["inputs"].append({
                "type": input_tag.attrs.get("type", "text"),
                "name": input_tag.attrs.get("name"),
                "value": input_tag.attrs.get("value", "")
            })
        return details

    def is_vulnerable(self, response):
        content = response.content.decode().lower()
        return any(error in content for error in self.vulnerable_errors)

    def scan_url(self, url):
        forms = self.get_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")

        for form in forms:
            details = self.get_form_details(form)
            for c in "\"'":
                data = {}
                for input_tag in details["inputs"]:
                    if input_tag["type"] in ("hidden", "submit"):
                        data[input_tag["name"]] = input_tag["value"] + c
                    else:
                        data[input_tag["name"]] = f"test{c}"

                target_url = urljoin(url, details["action"])
                try:
                    if details["method"] == "post":
                        res = self.session.post(target_url, data=data, timeout=self.timeout)
                    else:
                        res = self.session.get(target_url, params=data, timeout=self.timeout)

                    if self.is_vulnerable(res):
                        print(f"[!] SQL Injection vulnerability detected in form at {target_url}")
                        return True  # Return early if vulnerability found
                except requests.exceptions.RequestException as e:
                    print(f"[-] Error testing {target_url}: {e}")
        return False
    
    def sql_injector_manager():
        target_url = input('Insert an url: ')
        is_vulnerable = scan_url(target_url)

        if is_vulnerable:
            print("Vulnerabilità SQL Injection trovata!")
        else:
            print("Nessuna vulnerabilità trovata.")