# Falcon
Falcon is a CLI multitool for cybersecurity, available only for unix based operating systems.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---
## Installation
1. copy and paste the command on terminal.
```bash
wget https://raw.githubusercontent.com/rykerwilder/falcon/main/installer.sh && chmod +x installer.sh
```

2. run the installer
```bash
bash ./installer.sh
```

After running the installer, follow the instructions in your terminal to activate Sentinel.

---

## Menu

#### 1. Sherlock

is a Python-based OSINT (Open Source Intelligence) tool that searches for usernames across multiple social media platforms and websites. The tool runs asynchronously using a thread pool executor to perform searches without blocking the main application. When executed, it prompts for a target username and an optional timeout value (default: 10 seconds), then searches across hundreds of websites simultaneously. Results are automatically saved to a text file in the `./data/` directory with the format `username.txt`, containing all discovered profiles and their URLs. The search process runs in a separate thread, allowing the main menu to remain responsive. You can read more on their repo [sherlock-project](https://github.com/sherlock-project/sherlock).

#### 2. System Info
is a Python program designed to collect and display detailed information about the system on which it runs. It is useful for diagnosing hardware/software issues, monitoring system resources, or simply getting a comprehensive report of computer specifications. System info reports system data such as OS, RAM usage, CPU information, all disk partitions and their space, network information such as public, private, and MAC address.

#### 3. IP Tracker
is a Python program that extends the functionality of System info to provide detailed information about public IP addresses and domains. Use the [ip-api.com](https://ip-api.com/) public API to get geographic data, ISPs, and other useful information.
With IP Tracker you can view the information relating to your IP address or by choosing the second option you can view another IP address.

#### 4. Holehe

is an email OSINT tool that checks if an email address is associated with various online services and platforms. By querying multiple websites and social media platforms, Holehe reveals where a given email has been registered without requiring authentication. The tool provides a comprehensive report showing which services (social networks, forums, dating sites, etc.) are linked to the investigated email address. You can read more on their repo [olehe](https://github.com/megadose/holehe).

#### 5. Encrypted Chat (P2P)
is a secure peer-to-peer encrypted chat application that provides end-to-end encryption using RSA cryptography. This decentralized chat solution allows two users to communicate directly without intermediaries, ensuring privacy and security through 3072-bit key.

#### 6. Get Websites Cookies
is a web analysis tool that extracts and analyzes cookies from websites. It connects to any URL and retrieves detailed information about all cookies set by the server, including their names, values, domains, paths, security flags, and expiration dates. The tool handles redirects automatically and provides comprehensive reporting by saving all cookie data to a timestamped results file.

#### 7. WHOIS Domain Lookup
is a domain information tool that queries WHOIS databases to retrieve comprehensive registration details for any domain name. Using the python-whois library, it provides detailed information including domain ownership, registration dates, expiration dates, name servers, registrar information, and domain status.

#### 8. DNS Inspector

is a DNS analysis tool that performs comprehensive DNS record lookups for any domain name. Using the dnspython library, it queries multiple DNS record types including A (IPv4), AAAA (IPv6), MX (mail servers), TXT (text records), NS (name servers), and CNAME (canonical names). The tool provides detailed information about domain configuration and DNS infrastructure, handling various DNS response scenarios such as non-existent domains, timeouts, and server errors.

#### 9. Metadata Extractor

is a comprehensive file analysis tool that extracts and displays detailed metadata from various file types. The tool supports multiple formats including images (JPEG, PNG, etc.), videos, audio files, PDFs, and Microsoft Word documents. For images, it retrieves EXIF data, dimensions, and format information using PIL/Pillow. For videos, it extracts codec details, resolution, frame rate, duration, and bitrate information via pymediainfo. Audio files are analyzed using mutagen to obtain duration, bitrate, sample rate, and embedded tags. PDF files are inspected with PyPDF2 to retrieve page count and document properties, while DOCX files are analyzed using python-docx to extract author information, creation/modification dates, and document structure. All files receive basic metadata including file size, MIME type, and filesystem timestamps (creation, modification, and access dates). The extracted metadata is formatted into a readable report and automatically saved to a results file in the ./data/ directory.