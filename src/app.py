#!/usr/local/bin/python3
from commands import loop, highlighter
from utilities import Connected
def error_handler():
        highlighter.warn("You are not connected to the internet, do you still want to launch CWShell? Please note that a lot of the commands might not work")
        d = input("[Y/N]? ")
        if d.strip().lower() == "y":
            loop.start()
        elif d.strip().lower() == "n":
            exit()
        else:
            highlighter.error("You must select either Yes [Y] or No [N]")
            error_handler()

if __name__ == "__main__":
    if Connected():
        loop.start()
    else:
        error_handler()
    