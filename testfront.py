import socket

HOST = socket.gethostname()

PORT = 3006
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

print "connect"

while True:
	msg = tcp.recv(1024)
	print msg