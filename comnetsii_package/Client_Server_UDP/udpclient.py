from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
server = ('127.0.0.1', 8888)
s.sendto("comnetsii", server)
data, addr = s.recvfrom(1024)
print("received", data, "from", addr)
s.close()