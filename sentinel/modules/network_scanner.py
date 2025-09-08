import socket

def scan_ports(target, start_port=0, end_port=9999):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout for responsiveness
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

# Example usage: Scan localhost for ports 20 to 25
scan_ports("192.168.3.149", 0, 9999)