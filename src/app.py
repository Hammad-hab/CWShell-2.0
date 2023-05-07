#!/opt/homebrew/bin/python3
from commands import loop
from cli import highlighter
from utilities import Connected, input


def error_handler():
    highlighter.warn(
        "You are not connected to the internet, do you still want to launch CWShell? Please note that a lot of the commands might not work")
    d = input("[Y/N]? ")
    if d.strip().lower()[0] == "y":
        loop.start()
    elif d.strip().lower()[0] == "n":
        exit()
    else:
        highlighter.error("You must select either Yes [Y] or No [N]")
        error_handler()


if __name__ == "__main__":
    if Connected() :
        loop.start()
    else:
        error_handler()
