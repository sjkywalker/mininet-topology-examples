from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

Single3 = SingleSwitchTopo(k=3)

net = Mininet(topo=Single3)

net.start()
net.pingAll()
net.stop()

