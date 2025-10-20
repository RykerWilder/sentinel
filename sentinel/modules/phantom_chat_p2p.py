from colorama import Style, Fore
from sentinel import cleanup
import rsa
import socket
import threading
import sys 
from sentinel.modules.system_info import SystemInfo

class P2P(SystemInfo):
    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(3072)
        self.client = None
        self.public_partner = None
        self.running = True

    def p2p_manager(self):
        print(f"\n{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Your local IP is: {self.get_local_ip()}")
        
        default_port = 9999
        try:
            port = int(input(f"\n{Fore.CYAN}┌─[Insert port (default: {default_port}] \n└──> {Style.RESET_ALL}") or default_port)
        except ValueError:
            print(f"{Fore.RED}[X] Invalid port, using default: {default_port}{Style.RESET_ALL}")
            port = default_port

        while True:
            choice = input(f"\n{Fore.CYAN}┌─[Choose mode - Host (1) or Client (2)] \n└──> {Style.RESET_ALL}")
            if choice in ("1", "2"):
                break
            print(f"{Fore.RED}[X] Invalid choice.{Style.RESET_ALL}")

        #START CONNECTION
        if choice == "1":
            if not self.ip_address:
                self.ip_address = input(f"\n{Fore.CYAN}┌─[Enter your IP address] \n└──> {Style.RESET_ALL}")
            ip_address = self.ip_address
        else:
            ip_address = input(f"\n{Fore.CYAN}┌─[Enter host IP] \n└──> {Style.RESET_ALL}")
        
        if choice == "1":
            self.client, self.public_partner = self.create_host(ip_address, port)
        else:
            self.client, self.public_partner = self.create_connection(ip_address, port)

        print(f"\n{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Connection established.")

        #START THREAD
        self.start_chat_threads()

    def create_host(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind((ip, port))
            server.listen()
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Server listening on {ip}:{port}")
            
            client, addr = server.accept()
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Connection from {addr[0]}")
            
            #KEYS CHANGE
            client.send(rsa.PublicKey.save_pkcs1(self.public_key, "PEM"))
            partner_key = rsa.PublicKey.load_pkcs1(client.recv(1024), "PEM")
            
            return client, partner_key
        except Exception as e:
            print(f"{Fore.RED}[X] Server error: {e}{Style.RESET_ALL}")
            sys.exit(1)

    def create_connection(self, ip, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((ip, port))
            print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Connected to {Fore.MAGENTA}{ip}:{port}{Style.RESET_ALL}")
            
            #KEYS CHANGE
            partner_key_data = client.recv(1024)
            client.send(rsa.PublicKey.save_pkcs1(self.public_key, "PEM"))
            partner_key = rsa.PublicKey.load_pkcs1(partner_key_data, "PEM")
            
            return client, partner_key
        except Exception as e:
            print(f"{Fore.RED}[X] Connection error: {e}{Style.RESET_ALL}")
            sys.exit(1)

    def start_chat_threads(self):
        send_thread = threading.Thread(target=self.send_messages)
        recv_thread = threading.Thread(target=self.receive_messages)
        
        send_thread.daemon = True
        recv_thread.daemon = True
        
        send_thread.start()
        recv_thread.start()
        
        send_thread.join()
        recv_thread.join()

    def send_messages(self):
        try:
            while self.running:
                msg = input().strip()

                if not msg:
                    print(f"{Fore.RED}[X] Message can't be empty.{Style.RESET_ALL}")
                    continue

                encrypted = rsa.encrypt(msg.encode(), self.public_partner)
                self.client.send(encrypted)
                print(f"{Fore.MAGENTA}You:{Style.RESET_ALL} {msg}")
        except Exception as e:
            if self.running:
                print(f"{Fore.RED}[X] Send error: {e}{Style.RESET_ALL}")
        finally:
            cleanup(self)

    def receive_messages(self):
        try:
            while self.running:
                encrypted = self.client.recv(1024)
                if not encrypted:
                    break
                    
                msg = rsa.decrypt(encrypted, self.private_key).decode()
                print(f"\n{Fore.MAGENTA}Partner:{Style.RESET_ALL} {msg}\nYou: ", end="", flush=True)
        except Exception as e:
            if self.running:
                print(f"{Fore.RED}[X] Receive error: {e}{Style.RESET_ALL}")
        finally:
            cleanup(self)