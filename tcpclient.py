import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


port = 5555

client_socket.connect(("192.168.1.162",port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode("ascii"))