import platform
import socket
import psutil
import requests
from datetime import datetime

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
    print("\n" + "="*40 + " System Info " + "="*40)
    print(f"OS: {get_os_info()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Public IP: {get_public_ip()}")
    print(f"Local IP: {get_local_ip()}")
    print(f"CPU: {platform.processor()} ({psutil.cpu_count(logical=True)} cores)")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")

    # Spazio su disco
    print("\n Storage")
    for disk in get_disk_usage():
        print(f"  {disk['device']} ({disk['mountpoint']}):")
        print(f"    Total: {disk['total']} GB, Used: {disk['used']} GB ({disk['percent']}%)")

    print("=" * 45 + "\n")

if __name__ == "__main__":
    print_system_info()