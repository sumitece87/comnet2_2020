#/usr/bin/python
#Comnetsii APIs for Packet. Rutgers ECE423/544
#Author: Sumit Maheshwari
import time
from socket import socket, AF_INET, SOCK_DGRAM
import struct
import select
import random
import asyncore

def create_packet(pkttype, src, dst, seq, data):
    """Create a new packet based on given id"""
    # Type(1),  LEN(4), SRCID(1),  DSTID(1), SEQ(4), DATA(1000)  
    pktlen = len(data)
    header = struct.pack('BLBBL', pkttype, pktlen, dst, src, seq)
    return header + data

def read_header(pkt):
	#Change the bytes to account for network encapsulations
    header = pkt[0:16]
    #pktFormat = "BLBBL"
    #pktSize = struct.calcsize(pktFormat)
    pkttype, pktlen, dst, src, seq = struct.unpack("BLBBL", header)
    return pkttype, pktlen, dst, src, seq

def read_data(pkt):
	#Change the bytes to account for network encapsulations
    data = pkt[16:]
    return data

# def send_packet(pkt, dst_addr):
    # """
    # Sends a packet to the dest_addr using the UDP socket
    # """
    # my_socket = socket(AF_INET, SOCK_DGRAM)
    # my_socket.sendto(pkt, (dst_addr, 1))
    # my_socket.close()
    # print("Sent packet to the destination: ", dst_addr)
    # return 0

# def receive_packet(my_addr, port_num):
    # """
    # Listens at an IP:port
    # """
    # my_socket = socket(AF_INET, SOCK_DGRAM)
    # my_socket.bind((my_addr, port_num))
    # while True:
        # data, addr = my_socket.recvfrom(1024)
        # print("Received packet", data, "from source", addr)
        # if stop_thread:
            # break    




