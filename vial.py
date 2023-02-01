#!/usr/bin/python
from argparse import ArgumentParser
from colorama import Fore, Back, Style
from keystone import *
import ctypes, struct, sys

# ViAL - m0rtal

__bn  ='''
Y88b      / 888      e      888     
 Y88b    /  888     d8b     888     ViAL ---
  Y88b  /   888    /Y88b    888     venomous injected artifact library
   Y888/    888   /  Y88b   888     
    Y8/     888  /____Y88b  888     m0rtal
     Y      888 /      Y88b 888____
'''

__GLOBAL_QMODE = False

def display_banner():
    print(highlight(Fore.GREEN, __bn))

def highlight(color, text):
    return color + text + Style.RESET_ALL

if __name__ == '__main__':
    argp = ArgumentParser(prog='vial')
    argp.add_argument('--quiet', '-q', action='store_true', help='do not display the startup banner')
    args = argp.parse_args()

    if not args.quiet:
        display_banner()