#!/usr/local/bin/python3
from Socket import Client
import sys
c = Client()
c.watch("192.168.43.50", int(sys.argv[1]))
# c.watch("127.0.0.1", int(sys.argv[1]))