import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style
from falcon import write_to_result_file

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
            2: "Fixed line or mobile",
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
    
    def format_results(self, info):
        result = []
        result.append("="*60)
        result.append("PHONE NUMBER LOOKUP RESULTS")
        result.append("="*60)
        result.append(f"Valid number: {'yes' if info['valid'] else 'no'}")
        result.append(f"Possible number: {'yes' if info['possible'] else 'no'}")
        result.append(f"International: {info['international']}")
        result.append(f"National: {info['national']}")
        result.append(f"E164: {info['e164']}")
        result.append(f"RFC3966: {info['rfc3966']}")
        result.append(f"Location: {info['location']}")
        result.append(f"Country: {info['country']}")
        result.append(f"Country code: {info['country_code']}")
        result.append(f"National number: {info['national_number']}")
        result.append(f"Line type: {info['type']}")
        result.append(f"Carrier: {info['carrier'] if info['carrier'] else 'N/A'}")
        result.append("Timezones:")
        for tz in info['timezones']:
            result.append(f"   • {tz}")
        result.append("="*60)
        
        return "\n".join(result)
    
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
            
            format_results = self.format_results(info)
            
            filename = write_to_result_file(format_results, "NumberLookup")
            
            if filename:
                print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Results saved to: {filename}")
            else:
                print(f"{Fore.RED}[X] Error saving results{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")