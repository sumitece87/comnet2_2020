#Author: Keith Kuchenbrod
To test ping program run in the order below and on the corresponding nodes. All starting from mininet@mininet-vm

1. sudo python topo6.py
2. In mininet --> xterm h1 h2 r1 r2 
3. In h2 terminal --> python3.5 udpserver.py
4. In r2 terminal --> python3.5 udprouter2.py
5. In r1 terminal --> python3.5 udprouter1.py
6. In h1 terminal --> python3.5 udpclient.py