import shutil
from colorama import Style, Fore
import os
import datetime
import sys
import socket
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def clickable_link(url, text):
    return f"{Fore.CYAN}\033]8;;{url}\033\\{text}\033]8;;\033\\{Style.RESET_ALL}"

def print_welcome_message():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo = r"""
          _____        __                               .---.        .-----------
        _/ ____\____  |  |   ____  ____   ____         /     \  __  /    ------
        \   __\\__  \ |  | _/ ___\/  _ \ /    \       / /     \(  )/    -----
         |  |   / __ \|  |_\  \__(  (_) )   |  \     //////   ' \/ `   ---
         |__|  (____  /____/\___  >____/|___|  /    //// / // :    : ---
                    \/          \/           \/    // /   /  /`    '--
                                                  //          //..\\
                                                         ====UU====UU====                                  
    """
    welcome_message = f"""
        {Fore.MAGENTA}{logo}{Style.RESET_ALL}
        {Fore.CYAN}[INFO]{Style.RESET_ALL} If you want to read more about Falcon, go read {clickable_link('https://github.com/RykerWilder/sentinel', 'documentation')}.
        {Fore.CYAN}[INFO]{Style.RESET_ALL} Press CTRL+C to abort
    """
    print(welcome_message)

def print_dynamic_dots(key, value):
    #TERMINAL WIDTH
    cols = shutil.get_terminal_size().columns
    
    #DOTS LENGTH
    available_space = cols - len(key) - len(str(value)) - 3  
    
    print(f"{Fore.MAGENTA}{key}{Style.RESET_ALL}: {'.' * available_space} {value}")

def write_to_result_file(content, tool=""):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data_folder = "./data"
        
    #CREATE FOLDER IF NOT EXISTS
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        
    #PATH
    filename = os.path.join(data_folder, f"result_{tool}_{current_datetime}.txt")
        
    try:
        #WRITE CONTENT
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {content}\n")
        return filename
    except Exception as e:
        print(f"{Fore.RED}[X] Error writing file: {e}{Style.RESET_ALL}")
        return None

def exit(signum, frame):
    print(f"\n{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Aborted")
    sys.exit(0)

def cleanup(instance):
    if not instance.running:
        return
            
    instance.running = False
    if instance.client:
        try:
            instance.client.shutdown(socket.SHUT_RDWR)
            instance.client.close()
        except:
            pass
    print(f"\n{Fore.CYAN}[INFO]{Style.RESET_ALL} Connection closed.{Style.RESET_ALL}")
    sys.exit(0)

def create_map(position=None, lat=None, lon=None, zoom=10, output_file="data/map.html"):
    if position:
        try:
            geolocator = Nominatim(user_agent="mappa_generator")
            location = geolocator.geocode(position, timeout=10)
            
            if location is None:
                raise ValueError(f"{Fore.RED}[X] Unable find position: {position}{Style.RESET_ALL}")
            
            lat = location.latitude
            lon = location.longitude
            location_address = location.address
            
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            raise Exception(f"{Fore.RED}[X] Geodecoding error: {e}{Style.RESET_ALL}")
    else:
        location_address = f"Lat: {lat}, Lon: {lon}"
    
    #CREATE MAP
    mappa = folium.Map(
        location=[lat, lon],
        zoom_start=zoom,
        tiles='OpenStreetMap'
    )
    
    #ADD MARKER
    folium.Marker(
        location=[lat, lon],
        popup=location_address,
        tooltip="Click for more info",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mappa)
    
    folium.Circle(
        location=[lat, lon],
        radius=300,
        color='blue',
        fill=True,
        fillColor='blue',
        fillOpacity=0.2,
        popup=f'Area around {location_address}'
    ).add_to(mappa)
    
    #SAVE FILE
    mappa.save(output_file)
    print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Map saved in: {output_file}")
    
    return output_file