import socket

#What is Socket?
#IP address + Port number = Socket

#creating a socket object
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.getbyhostname()
port = 5555

#binding the host and the port
server_socket.bind((host,port))

#Listening for the incoming conection. In this case I have mentioned maximum of 5 connections
server_socket.listen(5)

while True:
	#Accepting the connection from client
	client_socket,address = server_socket.accept()
	print(f"received connection from {address}")

	message = "Thank you for connecting to the server"
	client_socket.send(message)
	client_socket.close()
