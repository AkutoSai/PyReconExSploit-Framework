import os
import sys
import time

from pyfiglet import Figlet


def run():
    f = Figlet(font='slant')
    f.renderText("Tutorial")
    start = """
Welcome to the PyReconExSploit Tutorial

    """
    animated(start)
    input("Press Enter To Continue...")
    os.system("clear")
    second = """
What is PyReconExSploit?

PyReconExSploit is a Reconnaissance and Exploitation framework
written in Python3. The framework is equipped with different types 
of tools which are used for Information Gathering, Cryptology, 
Exploitation and more.

    """
    animated(second)
    input("Press Enter To Continue...")


def animated(msg):
    for char in msg:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
