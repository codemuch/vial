#!/usr/bin/python
from argparse import ArgumentParser
from colorama import Fore, Back, Style
from enum import Enum
from keystone import *
import ctypes, struct, sys

# ~ DO NOT RUN ~
# This probably doesn't work and is just leftover from the rewrite.
# Keeping it here for now in case there's anything in here I still need
# to port over to vial.py.

__bn  ='''
Y88b      / 888      e      888     
 Y88b    /  888     d8b     888     ViAL ---
  Y88b  /   888    /Y88b    888     venomous injected assembly library
   Y888/    888   /  Y88b   888     
    Y8/     888  /____Y88b  888      
     Y      888 /      Y88b 888____
'''

__GLOBAL_QMODE = False

Egg = Enum('Egg', ['IsBadReadPtr', 'NtAccessCheck', 'NtDisplayString', 'SEH'])
Payload = Enum('Payload', ['Bind Download Execute Reverse'])

def display_banner():
    print(highlight(Fore.GREEN, __bn))

def err_die(err):
    print("%s %s" % (highlight(Fore.RED, '[ERROR]'), err))

def highlight(color, text):
    return color + text + Style.RESET_ALL

def print_encoded_ip(ip_addr):
    li = ["{:>02}".format(hex(int(i)).split('x')[1]) for i in ip_addr.split('.')]
    li.reverse()

    print("\n🧪 Encoding IPv4 address: %s" % ip_addr)
    print("🧪 Result: 0x%s" % ''.join(li))

def print_encoded_port(port_no):
    port_dec = "{:>04}".format(hex(int(port_no)).split('x')[1])
    port_hex = [port_dec[i:i+2] for i in range(0, len(port_dec), 2)]
    port_hex.reverse()

    print("\n🧪 Encoding port: %s" % port_no)
    print("🧪 Result: 0x%s" % ''.join(port_hex))

def resolve_symbol(dll, symbol):
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetModuleHandleA(dll.encode(encoding='ascii'))
    addr = kernel32.GetProcAddress(handle, symbol.encode(encoding='ascii'))
    print("🧪 Result:" % hex(addr))
    
def generate_egghunter(egghunter):
    if egghunter.lower() == Egg.IsBadReadPtr.name.lower():
        eh_type = 'isBadReadPtr'
    elif egghunter.lower() == Egg.NtAccessCheck.name.lower():
        eh_type = 'NtAccessCheck'
    elif egghunter.lower() == Egg.NtDisplayString.name.lower():
        eh_type = 'NtDisplayString'
    elif egghunter.lower() == Egg.SEH.name.lower():
        eh_type = 'SEH'
    else:
        sys.exit(1) # This shouldn't ever happen
    
    print("🧪 Generating %s egghunter:" % eh_type)
    code = ""
    with open('vials/egghunter/%s.nasm' % egghunter.lower(), 'r') as file:
        code = ''.join(file.readlines())
    file.close()
    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    encoding, count = ks.asm(code)
    egghunter = ""
    for dec in encoding:
        egghunter += "\\x{0:02x}".format(int(dec)).rstrip("\n")

    print("\"" + highlight(Fore.GREEN, egghunter) + "\"")
    

if __name__ == '__main__':
    argp = ArgumentParser(prog='vial')
    argp.add_argument('--badchars', '-b', action='store', type=str)
    argp.add_argument('--egghunter', action='store', type=str)
    argp.add_argument('--encode-ip', '--ip', action='store', type=str)
    argp.add_argument('--encode-port', '--p', action='store', type=str)
    argp.add_argument('--no-warn', '--n')
    argp.add_argument('--quiet', '--q', '-q', action='store_true', help='do not display the startup banner')
    argp.add_argument('--resolve', '--r', action='store', help='resolve the address of a symbol for a given module')
    args = argp.parse_args()

    if not args.quiet:
        display_banner()

    if args.egghunter:
        if args.egghunter.lower() in [m.lower() for m in Egg.__members__]:
            generate_egghunter(args.egghunter)
        else:
            err_die('Invalid egg hunter specified. Options: IsBadReadPtr, NtAccessCheck, NtDisplayString, SEH')

    if args.encode_ip:
        print_encoded_ip(args.encode_ip)

    if args.encode_port:
        print_encoded_port(args.encode_port)
