import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

class PhoneNumberLookup:
    def validate_phone_number(self, number):
        try:
            parsed = phonenumbers.parse(number, None)
            if phonenumbers.is_valid_number(parsed):
                return parsed
            else:
                return None
        except phonenumbers.phonenumberutil.NumberParseException:
            return None

    def get_phone_info(self, phone_number):
        info = {}
        
        info['valid'] = phonenumbers.is_valid_number(phone_number)
        info['possible'] = phonenumbers.is_possible_number(phone_number)
        
        info['international'] = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        info['national'] = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.NATIONAL
        )
        info['e164'] = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.E164
        )
        info['rfc3966'] = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.RFC3966
        )

        info['country'] = geocoder.description_for_number(phone_number, "it")
        info['location'] = geocoder.description_for_number(phone_number, "en")
        
        info['carrier'] = carrier.name_for_number(phone_number, "it")

        timezones = timezone.time_zones_for_number(phone_number)
        info['timezones'] = list(timezones) if timezones else ["N/A"]
        
        number_type = phonenumbers.number_type(phone_number)
        type_map = {
            0: "Fixed line",
            1: "Mobile",
            2: "Fixed line or mobile ",
            3: "Toll free",
            4: "Premium rate",
            5: "Shared cost",
            6: "VOIP",
            7: "Personal number",
            8: "PAGER",
            9: "Universal Access Number",
            10: "Voicemail",
            99: "Unknown"
        }
        info['type'] = type_map.get(number_type, "UNKNOWN")
        
        info['country_code'] = f"+{phone_number.country_code}"
        info['national_number'] = phone_number.national_number
        
        return info

    def display_results(self, info):
        print("RESULTS")

        print(f"   Valid number: {'yes' if info['valid'] else 'no'}")
        print(f"   Possible number: {'yes' if info['possible'] else 'no'}")

        print(f"   International: {info['international']}")
        print(f"   National: {info['national']}")
        print(f"   E164: {info['e164']}")
        print(f"   RFC3966: {info['rfc3966']}")

        print(f"   Location: {info['location']}")
        print(f"   Country: {info['country']}")
        print(f"   Country code: {info['country_code']}")
        print(f"   National number: {info['national_number']}")

        print(f"   Line type: {info['type']}")
        print(f"   Carrier: {info['carrier'] if info['carrier'] else 'N/A'}")

        for tz in info['timezones']:
            print(f"   • {tz}")
        
        print("\n" + "="*60)



    def phone_number_lookup_manager(self):
        phone_input = input(f"\n{Fore.CYAN}┌─[Insert number to check] \n└──> {Style.RESET_ALL}").strip()
        
        if not phone_input:
            print(f"{Fore.RED}[X] Number not found{Style.RESET_ALL}")
            return
        
        parsed_number = self.validate_phone_number(phone_input)
        
        if parsed_number is None:
            print(f"{Fore.RED}[X] Error: Invalid number or unrecognized format{Style.RESET_ALL}")
            return
        
        try:
            info = self.get_phone_info(parsed_number)
            self.display_results(info)
        
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")