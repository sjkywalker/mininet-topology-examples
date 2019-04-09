# Mininet Topology Examples

Sample python codes for emulating network topology with `Mininet`

## Language

venv=2.7

## Handling Errors

```
File "/usr/lib/python2.7/dist-packages/mininet/net.py", line 172, in __init__
self.build()
File "/usr/lib/python2.7/dist-packages/mininet/net.py", line 442, in build
self.buildFromTopo( self.topo )
File "/usr/lib/python2.7/dist-packages/mininet/net.py", line 409, in buildFromTopo
self.addController( 'c%d' % i, cls )
File "/usr/lib/python2.7/dist-packages/mininet/net.py", line 261, in addController
controller_new = controller( name, **params )
File "/usr/lib/python2.7/dist-packages/mininet/node.py", line 1518, in DefaultController
raise Exception( 'Could not find a default OpenFlow controller' )
Exception: Could not find a default OpenFlow controller
```

This error occurs because default controller is not recognized. Resolve by installing the controller and creating a symlink.

```
$ sudo apt-get install openvswitch-testcontroller
$ sudo ln /usr/bin/ovs-testcontroller /usr/bin/controller 
```

## Acknowledgements

* [James Sung](https://github.com/sjkywalker/)
* [Stackoverflow: Mininet cannot find required executable controller](https://stackoverflow.com/questions/17341076/mininet-cannot-find-required-executable-controller)
* [CS154, Ateneo de Manila University](http://cgweb1.northumbria.ac.uk/SubjectAreaResources/EN0746/lec09.pdf)

