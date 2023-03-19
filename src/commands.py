#!/usr/bin/python3
from cli import Environment, loop  # see cli.py
from basic_commands import cname, Exit
from Server import server
from Client import client
# Adding the basic commands into the command enviornment
Environment.add(cname, Exit)
# By adding the commands into the command enviornment, we are basically
# making those commands available in the runtime enviornment. By commenting this line
# you are removing basic commands such as “exit“ and “info“.
# Read the cli.py source for more information
Environment.add(server,client)