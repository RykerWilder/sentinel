import platform
import socket
import psutil
import requests
import shutil
from colorama import Style, Fore
from .utils import print_dynamic_dots

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org?format=json").json().get("ip", "not available")
    except:
        return "not available"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return socket.gethostbyname(socket.gethostname())

def get_os_info():
    system = platform.system()
    if system == "Darwin":
        return f"macOS {platform.mac_ver()[0]}"
    elif system == "Windows":
        return f"Windows {platform.release()}"
    elif system == "Linux":
        return f"Linux {platform.release()}"
    else:
        return system

def get_disk_usage():
    disks = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "total": round(usage.total / (1024 ** 3), 2),
                "used": round(usage.used / (1024 ** 3), 2),
                "free": round(usage.free / (1024 ** 3), 2),
                "percent": usage.percent
            })
        except:
            continue
    return disks

def print_system_info():
    print(f"\n{'='*40}{Fore.CYAN} SysInsider {Style.RESET_ALL}{'='*40}")
    print_dynamic_dots('OS', get_os_info())
    print_dynamic_dots('Hostname', socket.gethostname())
    print_dynamic_dots('Public IP', get_public_ip())
    print_dynamic_dots('Local IP', get_local_ip())
    print_dynamic_dots('CPU', f"platform.processor() (psutil.cpu_count(logical=True) cores)")
    print_dynamic_dots('RAM', f"round(psutil.virtual_memory().total / (1024 ** 3), 2) GB")

    # Spazio su disco
    print("Storage: ")
    for disk in get_disk_usage():
        print(f"  {disk['device']} ({disk['mountpoint']}):")
        print(f"    Total: {disk['total']} GB, Used: {disk['used']} GB ({disk['percent']}%)")
    
    terminal_width = shutil.get_terminal_size().columns #terminal width
    print("=" * terminal_width + "\n")

if __name__ == "__main__":
    print_system_info()