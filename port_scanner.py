import socket

def port_scanner(target, ports):
    clcoding = socket.gethostbyname(target)
    print(f"Scanning {target} ({clcoding})")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((clcoding, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

target = "google.com"
ports = [21, 22, 80, 443, 8080]
port_scanner(target, ports)