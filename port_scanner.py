import socket
from IPy import IP

def scan(ip):
    converted_ip = check_ip(ip)
    print(f"[+]Scanning the target {str(ip)}")
    for port in range(400,500):
        scan_port(converted_ip,port)


def check_ip(ip_add):
    try:
        IP(ip_add)
        return ip_add
    except:
        return socket.gethostbyname(ip_add)

def get_banner(s):
    return s.recv(1024)


def scan_port(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip,port))
        try:
            banner = get_banner(sock)
            print("[+]Port" + str(port) + " : " + str(banner.decode().split("\n")))
        except:
            print(f"[+]Port {str(port)} is open")

    except:
        pass

targets = input("[+] Enter the target/s to scan (split the targets using ,: ")
if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "))
else:
    scan(targets)

print("All Done")