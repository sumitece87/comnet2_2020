from socket import socket, AF_INET, SOCK_DGRAM
from packet import *
from threading import Thread

#Creates new router
class udprouter():

        def __init__(self, id, port):
                self.port = port
                self.id = id
                self.rt = { 'routes': [{'id': 201, 'ip': '10.0.1.0', 'gateway': '10.0.1.1', 'port':8881},
                {'id': 102, 'ip': '192.168.2.1', 'gateway': '192.168.2.2', 'port':8883}
                ,{'id': 103, 'ip': '192.168.3.1', 'gateway': '192.168.3.2', 'port':8884}] }

        # Using the dst received in packet finds the corresponding dst address
        def search_dst_addr(self, dst):
                for x in range(len(self.rt['routes'])):
                        if self.rt['routes'][x]['id'] == dst:
                                return (self.rt['routes'][x]['ip'], self.rt['routes'][x]['port'])
                return ('10.0.1.0', 8881)

        # Sends packet to dst address
        def handle_sending(self, packet, server):
                s = socket(AF_INET, SOCK_DGRAM)
                s.sendto( packet, server )
                print('Sending To: ', server)
                s.close()
                return 0
            
        # Waits to receive a packet and if the correct type starts new thread to sent that packet
        def handle_packets(self):
                s = socket(AF_INET, SOCK_DGRAM)
                s.bind(('0.0.0.0', self.port))
                while True:
                        packet, addr = s.recvfrom(1024)
                        print("Received From: ", addr)
                        pkttype, pktlen, dst, src, seq = read_header(packet)
                        if pkttype == 1 or pkttype == 2:
                                server = self.search_dst_addr(dst)
                                thread = Thread(target=self.handle_sending(packet, server))
                                thread.start()
                s.close()
                return 0

if __name__ == '__main__':
        print("Router Started...")
        udp_router = udprouter(id=202, port=8882)
        udp_router.handle_packets()

