#!/usr/bin/python
from argparse import ArgumentParser
from colorama import Fore, Back, Style
from enum import Enum
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

Egg = Enum('Egg', ['IsBadReadPtr', 'NtAccessCheck', 'NtDisplayString', 'SEH'])


def display_banner():
    print(highlight(Fore.GREEN, __bn))

def err_die(err):
    print("%s %s" % (highlight(Fore.RED, '[ERROR]'), err))

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

def print_egghunter(egghunter):
    match egghunter:
        case Egg.IsBadReadPtr.name:
            print('isBadReadPtr')
        case Egg.NtAccessCheck.name:
            print('NtAccessCheck')
        case Egg.NtDisplayString.name:
            print('NtDisplayString')
        case Egg.SEH.name:
            print('SEH')

if __name__ == '__main__':
    argp = ArgumentParser(prog='vial')
    argp.add_argument('--egghunter', action='store', type=str)
    argp.add_argument('--encode-ip', '--ip', action='store', type=str)
    argp.add_argument('--encode-port', '--port', action='store', type=str)
    argp.add_argument('--quiet', '-q', action='store_true', help='do not display the startup banner')
    args = argp.parse_args()

    if not args.quiet:
        display_banner()

    if args.egghunter:
        if Egg.__members__.__contains__(args.egghunter):
            print_egghunter(args.egghunter)
        else:
            err_die('Invalid egg hunter specified. Options: IsBadReadPtr, NtAccessCheck, NtDisplayString, SEH')

    if args.encode_ip:
        print_encoded_ip(args.encode_ip)

    if args.encode_port:
        print_encoded_port(args.encode_port)