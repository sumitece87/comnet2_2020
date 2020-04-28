from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
from mininet.node import Node
from mininet.link import TCLink
from cleanup import cleanup
class Topo6( Mininet ):

    def __init__(self):
        Mininet.__init__(self, link=TCLink, controller=None, cleanup=True)

        #Creating Hosts
        info( "Creating nodes\n" )
        r1 = self.addHost( 'r1', inNamespace=False )
        r2 = self.addHost( 'r2', inNamespace=False )
        h1 = self.addHost( 'h1', inNamespace=False )
        h2 = self.addHost( 'h2', inNamespace=False )
        h3 = self.addHost( 'h3', inNamespace=False )

        #Establishing the links from hosts to routers
        info( "Creating links\n" )
        self.addLink( h1, r1, intfName2='r1-eth0')
        self.addLink( h2, r2, intfName2='r2-eth2')
        self.addLink( h3, r2, intfName2='r2-eth3')
        self.addLink( r1, r2, intfName1='r1-eth1', intfName2='r2-eth1', bw=10, delay='1ms', loss=10 )

        #Setting interface ip addresses since params1 or params2 just will not work
        host1 = self.get('h1')
        host2 = self.get('h2')
        host3 = self.get('h3')
        router1 = self.get('r1')
        router2 = self.get('r2')
        host1.setIP('192.168.1.1/24', intf='h1-eth0')
        host2.setIP('192.168.2.1/24', intf='h2-eth0')
        host3.setIP('192.168.3.1/24', intf='h3-eth0')
        router1.setIP('192.168.1.2/24', intf='r1-eth0')
        router1.setIP('10.0.1.0/24', intf='r1-eth1')
        router2.setIP('10.0.1.1/24', intf='r2-eth1')
        router2.setIP('192.168.2.2/24', intf='r2-eth2')
        router2.setIP('192.168.3.2/24', intf='r2-eth3')
        
        #Setting default routes for each interface
        h1.cmd( 'ip route add default via 192.168.1.2')
        h2.cmd( 'ip route add default via 192.168.2.2')
        h3.cmd( 'ip route add default via 192.168.3.2')
        r1.cmd( 'sysctl net.ipv4.ip_forward=1' )
        r2.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def start_network(self):
        CLI( self )

if __name__ == '__main__':
    topo = Topo6()
    topo.start_network()
    cleanup()
