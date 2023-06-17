# CWShell 2.0
## a bare minimum, open source implementation of remote control mechanism.
##### Current version:  `@2.1.1`

CWShell is a free open source project created in python to allow developers to quickly set up a remote control and/or command line/socket functionality for their application. No more hard core low level C-stuff is needed to get something up and running. Apart from that, CWShell also features various classes that'll help you create a two-way socket connection with ease and with control. Often in programming one observes that abstractions lead to lack of control. In CWShell there is a similar case but, in order to fix that problem, we allow users to both use the abstraction layer and the low-level socket according to their needs.

###  How do we do this?
Basically, the whole application's connection architecture is based on one class that's called `Socket` (See Socket.py) which has basic functions that let you send and receive data with abstractions but also with a property named ```.socket``` that gives you access to the socket that's being used. This means that you can choose between using the direct-access socket layer and the super easy abstractaction layer.
Not the best solution, but it works just fine.

### Other utilities provided by CWShell
### CLI (available at cli.py)
CLI (**C**reate your own command **L**ine interface **I**nstantly) is a simple library integrated and used in CWShell that allows you to get a simple Command line tool up and running within minutes. There isn't any documentation for it yet but there is a simple tutorial integrated in the source at `cli.py` in the form of doc-strings. Basically, the library contains three classes:
* Map
* Command
* CommandEnvionrment
* CommandLoop
That's it! A Map (in CWShell's cli library) is an object that contains information about the command (i.e parameters, description, long-name etc). A CommandEnviornment is just a containment wrapper defined to maintain an interface between a commands execution mechanism and the command loop which is responsible for creating a whatchamacallit loop.
The command loop does much more. Firstly, it helps in controlling keyboard interrupts, command history and variable stuff etc. Secondly, it helps you create prompts with emojis! For example, the CWShell Utility uses a shell emoji as a prompt.

### Misc Utilities
* GET_OS (*type: function*).
* Ip address fetcher (*type: function*).
* Socket (*type: class*) class that provides a cheap interface between python low-level socket API.
* CWSH_LANG (*type: class*). A bash execution environment that lets you define various kinds of commands. In CWShell, it was used to create a suitable BASH execution environment that returned data. Initially, CWShell lacked a suitable BASH execution Environment.
* CWSH_INT (*type: class*). This is just a CWShell utility, nothing more. It can be modified accordingly to accommodate your usage.
* compile (*type: function*). This is yet another utility for Open Source users. Basically it uses pyinstaller to compile the source according to the OS.
* install_packages (*type: function*). This is also a utility for open source users. It reads through the requirements.txt and instals those packages for you but if pip is not in the environment variables, it'll raise an exception.
 
***It is important to note that the name of these utilities might vary in different versions.***

### Resources
* [CWShell Website](https://hammad-hab.github.io/CWShell-2.0/)
* [CWShell 1.0 & 1.2](https://hammad-hab.github.io/CWShell/)
* [CWShell 2.0 Documentation](https://hammad-hab.github.io/CWShell-2.0/docs.htm)
* 
### Credits
The picture used as parallax is not owned by the creators of CWShell. All rights go to the respective owner. If someone wants to have it removed. Please report at the issues section

### Future updates
* Better documentation
* Better and more usable API
* Blacklisting feature
