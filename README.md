# CWShell 2.0
## a bare minimum, open source implementation of remote control.

CWShell is a free open source project created in python to alow developers to quickly set up a remote control functionality for their application. No more hard core low level C-stuff is needed to get something up and running. Apart from that, CWShell also features various classes that'll help you create a two-way socket connection with ease and with control. Often in programming on observes that abstractions lead to lack of control. In CWShell there is a similar case but, in order to fix that problem, we allow users to both use the abstraction layer and the low-level socket according to their needs.

###  How do we do this?
Basically, the whole application's connection architecture is based on one class that's called `Socket` (See Socket.py) which has basic functions that let you send and receive data with absractions but also with a property named ```.socket``` that gives you access to the socket that's being used. This means that you can choose between using the unabsracted socket layer and the super easy absractaction layer.
Not the best solution, but it works just fine.

### Reasources
* [CWShell Website](https://hammad-hab.github.io/CWShell-2.0/)
* [CWShell 1.0 & 1.2](https://hammad-hab.github.io/CWShell/)
* [CWShell 2.0 Documentation](https://hammad-hab.github.io/CWShell-2.0/docs.htm)
