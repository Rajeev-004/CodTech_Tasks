import socket

def port_scan(target, ports):
    print(f"\n[~] Scanning {target} for open ports...\n")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")

