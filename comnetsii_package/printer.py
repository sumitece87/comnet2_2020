#!/usr/bin/python
#Printer util for Rutgers comnetsii ECE423/544 
#Author: Sumit Maheshwari    
def get_host_ips(net):
    for host in net.hosts:
        print(host.name, host.IP())

def get_host_macs(net):
    for host in net.hosts:
        print(host.name, host.MAC())
    
def get_interfaces(net):
    for switch in net.switches:
        info(switch, "\n")
        for intfs in switch.intfList():
            info(intfs, switch.ports[intfs], '\n')
 
