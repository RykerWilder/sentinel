from colorama import Style, Fore
from sentinel import cleanup
import rsa
import socket
import threading

class P2P:
    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(3072)
        self.client = None
        self.public_partner = None
        self.running = True
        
        self.p2p_manager()

    def p2p_manager(self):
        print(f"\n{Fore.BLUE}[INFO]{Style.RESET_ALL} Your local IP is: {Fore.BLUE}{get_local_ip()}{Style.RESET_ALL}")
        
        default_port = 9999
        try:
            port = int(input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert port (default: {default_port}) => ") or default_port)
        except ValueError:
            print(f"{Fore.RED}[X] Invalid port {default_port}{Style.RESET_ALL}")
            port = default_port

        while True:
            choice = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Choose mode - Host [1] or Client [2] => ")
            if choice in ("1", "2"):
                break
            print(f"{Fore.RED}[X] Invalid choice{Style.RESET_ALL}")

        # START CONNECTION
        ip_address = get_local_ip() if choice == "1" else input(f"{Fore.GREEN}[?] Enter host IP: {Style.RESET_ALL}")
        
        if choice == "1":
            self.client, self.public_partner = self.create_host(ip_address, port)
        else:
            self.client, self.public_partner = self.create_connection(ip_address, port)

        print(f"\n{Fore.BLUE}[INFO]{Style.RESET_ALL} Connection established!")
        print(f"{Fore.YELLOW}[!] Press Ctrl+C to quit{Style.RESET_ALL}\n")

        # START THREAD
        self.start_chat_threads()

    def create_host(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind((ip, port))
            server.listen()
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Server listening on {Fore.CYAN}{ip}:{port}{Style.RESET_ALL}")
            
            client, addr = server.accept()
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Connection from {Fore.CYAN}{addr[0]}{Style.RESET_ALL}")
            
            # KEYS CHANGE
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
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Connected to {Fore.BLUE}{ip}:{port}{Style.RESET_ALL}")
            
            # Scambio chiavi
            client.send(rsa.PublicKey.save_pkcs1(self.public_key, "PEM"))
            partner_key = rsa.PublicKey.load_pkcs1(client.recv(1024), "PEM")
            
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
                    print(f"{Fore.RED}[!] Message can't be empty!{Style.RESET_ALL}")
                    continue

                encrypted = rsa.encrypt(msg.encode(), self.public_partner)
                self.client.send(encrypted)
                print(f"{Fore.YELLOW}You:{Style.RESET_ALL} {msg}")
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
                print(f"\n{Fore.BLUE}Partner:{Style.RESET_ALL} {msg}\nYou: ", end="", flush=True)
        except Exception as e:
            if self.running:
                print(f"{Fore.RED}[X] Receive error: {e}{Style.RESET_ALL}")
        finally:
            cleanup(self)