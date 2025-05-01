import platform
import socket
import psutil
import requests
import shutil
import uuid
from colorama import Style, Fore
from sentinel import print_dynamic_dots

class SysInsider:
    def __init__(self):
        # Verifica che il sistema sia Unix-like
        if platform.system() not in ['Linux', 'Darwin']:
            raise SystemExit("❌ Questo script può essere eseguito solo su sistemi Unix-like (Linux/macOS)")

    def get_public_ip(self):
        try:
            return requests.get("https://api.ipify.org?format=json").json().get("ip", "not available")
        except:
            return "Not available"

    def get_os_details(self):
        system = platform.system()
        details = {
            "system": system,
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture()[0],
            "machine": platform.machine()
        }

        if system == "Darwin":
            details["version"] = f"macOS {platform.mac_ver()[0]}"
        elif system == "Linux":
            # Per Linux, possiamo ottenere informazioni più dettagliate
            try:
                with open('/etc/os-release') as f:
                    os_info = {}
                    for line in f:
                        if '=' in line:
                            k, v = line.strip().split('=', 1)
                            os_info[k] = v.strip('"')
                    details["version"] = f"{os_info.get('PRETTY_NAME', 'Linux')}"
            except:
                details["version"] = f"Linux {platform.release()}"

        return details

    def get_cpu_info(self):
        cpu_info = {
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True)
        }

        # Metodi diversi per ottenere il nome del processore su Linux vs macOS
        if platform.system() == "Linux":
            try:
                with open('/proc/cpuinfo') as f:
                    for line in f:
                        if line.strip() and 'model name' in line.lower():
                            cpu_info["name"] = line.split(':')[1].strip()
                            break
            except:
                cpu_info["name"] = platform.processor()
        else:  # macOS
            cpu_info["name"] = platform.processor()

        return cpu_info

    def get_ram_info(self):
        mem = psutil.virtual_memory()
        return {
            "total": round(mem.total / (1024 ** 3), 2),
            "available": round(mem.available / (1024 ** 3), 2),
            "used": round(mem.used / (1024 ** 3), 2),
            "percent": mem.percent
        }

    def get_disk_usage(self):
        disks = []
        for partition in psutil.disk_partitions():
            # Su Unix, escludiamo i filesystem speciali
            if not partition.mountpoint.startswith(('/snap', '/dev', '/proc', '/run', '/sys')):
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

    def get_network_info(self):
        interfaces = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        return {
            "interfaces": {
                name: {
                    "addresses": [addr.address for addr in addrs if addr.family == socket.AF_INET],
                    "is_up": stats[name].isup if name in stats else False
                } for name, addrs in interfaces.items()
            }
        }

    def get_mac_address(self):
        # Ottiene l'indirizzo MAC della prima interfaccia attiva
        for name, data in self.get_network_info()["interfaces"].items():
            if data["is_up"] and name != "lo":  # esclude loopback
                for addr in psutil.net_if_addrs()[name]:
                    if addr.family == psutil.AF_LINK:
                        return addr.address
        return "Not available"

    def sys_insider_manager(self):
        terminal_width = shutil.get_terminal_size().columns
        print(f"\n{'='*40}{Fore.BLUE} SysInsider (Unix-only) {Style.RESET_ALL}{'='*40}")

        # OS Information
        os_details = self.get_os_details()
        print_dynamic_dots('OS', f"{os_details['version']} ({os_details['architecture']})")
        print_dynamic_dots('Hostname', socket.gethostname())

        # Hardware Information
        cpu = self.get_cpu_info()
        print_dynamic_dots('CPU', f"{cpu.get('name', 'Unknown')} ({cpu['cores']} cores, {cpu['threads']} threads)")

        ram = self.get_ram_info()
        print_dynamic_dots('RAM', f"{ram['total']} GB total, {ram['used']} GB used ({ram['percent']}%)")

        # Network Information
        print("Network:")
        print_dynamic_dots('  MAC Address', self.get_mac_address())
        print_dynamic_dots('  Public IP', self.get_public_ip())
        network_info = self.get_network_info()
        for name, data in network_info.get("interfaces", {}).items():
            if data.get("is_up", False) and data.get("addresses", []) and name != "lo":
                print_dynamic_dots(f"  {name}", f"{', '.join(data['addresses'])}")

        # Storage Information
        print("Storage:")
        for disk in self.get_disk_usage():
            print(f"  {disk['device']} ({disk['mountpoint']}):")
            print_dynamic_dots('    Total', f"{disk['total']} GB")
            print_dynamic_dots('    Used', f"{disk['used']} GB")
            print_dynamic_dots('    Percent', f"{disk['percent']}%")

        print("=" * terminal_width + "\n")
