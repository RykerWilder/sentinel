# Sentinel
Sentinel is a Swiss Army knife for cybersecurity, available only for unix based operating systems.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![sentinel](./assets/sentinel.png)

---
## Installation
To install sentinel you can copy and paste the command on terminal.

```bash
wget https://raw.githubusercontent.com/rykerwilder/sentinel/main/installer.sh && chmod +x installer.sh
```

**run installer**

```bash
bash ./installer.sh
```

After running the installer, follow the instructions in your terminal to activate Sentinel.

---

## Menu

#### 1. 

#### 2. System Info
is a Python program designed to collect and display detailed information about the system on which it runs. It is useful for diagnosing hardware/software issues, monitoring system resources, or simply getting a comprehensive report of computer specifications. System info reports system data such as OS, RAM usage, CPU information, all disk partitions and their space, network information such as public, private, and MAC address.

#### 3. IP Tracker
is a Python program that extends the functionality of System info to provide detailed information about public IP addresses and domains. Use the [ip-api.com](https://ip-api.com/) public API to get geographic data, ISPs, and other useful information.
With IP Tracker you can view the information relating to your IP address or by choosing the second option you can view another IP address.

#### 4. Packet Sniffer
is a Python network analysis tool that captures and analyzes network traffic in real-time using the Scapy library. It allows users to monitor packets on a specific network address, displaying detailed information about IP communications including source and destination addresses, and protocol-specific data (TCP ports, UDP ports, or ICMP). The sniffer runs for a configurable duration (default 30 seconds) and logs all captured packets to a results file, making it ideal for network diagnostics, security analysis, and traffic monitoring.

#### 5. Encrypted Chat (P2P)
is a secure peer-to-peer encrypted chat application that provides end-to-end encryption using RSA cryptography. This decentralized chat solution allows two users to communicate directly without intermediaries, ensuring privacy and security through 3072-bit key.

#### 6. Get Websites Cookies
is a web analysis tool that extracts and analyzes cookies from websites. It connects to any URL and retrieves detailed information about all cookies set by the server, including their names, values, domains, paths, security flags, and expiration dates. The tool handles redirects automatically and provides comprehensive reporting by saving all cookie data to a timestamped results file.

#### 7. WHOIS Domain Lookup
is a domain information tool that queries WHOIS databases to retrieve comprehensive registration details for any domain name. Using the python-whois library, it provides detailed information including domain ownership, registration dates, expiration dates, name servers, registrar information, and domain status.

#### 8. DNS Inspector

is a DNS analysis tool that performs comprehensive DNS record lookups for any domain name. Using the dnspython library, it queries multiple DNS record types including A (IPv4), AAAA (IPv6), MX (mail servers), TXT (text records), NS (name servers), and CNAME (canonical names). The tool provides detailed information about domain configuration and DNS infrastructure, handling various DNS response scenarios such as non-existent domains, timeouts, and server errors.