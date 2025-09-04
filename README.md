# Sentinel
Sentinel is a Swiss Army knife for cybersecurity, available only for unix operating systems.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![sentinel](./assets/sentinel.png)

---
## Installation

1. clone repository from github
```bash
git clone https://github.com/RykerWilder/sentinel.git
```

2. change directory in sentinel
```bash
cd sentinel
```

3. create a virtual environment (venv)
```bash
python3 -m venv venv
```

4. activate venv
```bash
source venv/bin/activate
```

5. install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

6. start project
```bash
python3 main.py
```

---

## Menu

#### 1. Network Scanner


#### 2. SysstemInfo
is a Python program designed to collect and display detailed information about the system on which it runs. It is useful for diagnosing hardware/software issues, monitoring system resources, or simply getting a comprehensive report of computer specifications. SysInsider reports system data such as OS, RAM usage, CPU information, all disk partitions and their space, network information such as public, private, and MAC address.

#### 3. IPGlobeTracker
is a Python program that extends the functionality of SysInsider to provide detailed information about public IP addresses and domains. Use the [ip-api.com](https://ip-api.com/) public API to get geographic data, ISPs, and other useful information.
With IPGlobeTracker you can view the information relating to your IP address or by choosing the second option you can view another IP address.

#### 4. Packet Sniffer
is a Python network analysis tool that captures and analyzes network traffic in real-time using the Scapy library. It allows users to monitor packets on a specific network address, displaying detailed information about IP communications including source and destination addresses, and protocol-specific data (TCP ports, UDP ports, or ICMP). The sniffer runs for a configurable duration (default 30 seconds) and logs all captured packets to a results file, making it ideal for network diagnostics, security analysis, and traffic monitoring.