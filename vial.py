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

def print_encoded_ip(ip_addr):
    li = ["{:>02}".format(hex(int(i)).split('x')[1]) for i in ip_addr.split('.')]
    li.reverse()

    print("\n🧪 You entered: %s" % ip_addr)
    print("🧪 Result: 0x%s" % ''.join(li))

def print_encoded_port(port_no):
    port_dec = "{:>04}".format(hex(int(port_no)).split('x')[1])
    port_hex = [port_dec[i:i+2] for i in range(0, len(port_dec), 2)]
    port_hex.reverse()

    print("\n🧪 You entered: %s" % port_no)
    print("🧪 Result: 0x%s" % ''.join(port_hex))

if __name__ == '__main__':
    argp = ArgumentParser(prog='vial')
    argp.add_argument('--quiet', '-q', action='store_true', help='do not display the startup banner')
    argp.add_argument('--encode-ip', '--ip', action='store', type=str)
    argp.add_argument('--encode-port', '--port', action='store', type=str)
    args = argp.parse_args()

    if not args.quiet:
        display_banner()
    
    if args.encode_ip:
        print_encoded_ip(args.encode_ip)

    if args.encode_port:
        print_encoded_port(args.encode_port)