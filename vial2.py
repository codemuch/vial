#!/usr/bin/python

import argparse
import sys
from rich.console import Console

BANNER = '''[green]
Y88b      / 888      e      888     
 Y88b    /  888     d8b     888     ViAL ---
  Y88b  /   888    /Y88b    888     venomous injected assembly library
   Y888/    888   /  Y88b   888     
    Y8/     888  /____Y88b  888     
     Y      888 /      Y88b 888____
[/green]'''

DEFAULT_TAG = 'y0y0'

def tag_to_hex(s):
    if len(s) == 4:
        tag = s
    else:
        console.error()
        tag = DEFAULT_TAG
    return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"

def main(args):
    console = Console()
    console.print(BANNER)

    if args.egghunter:
        tag = args.tag

        if len(tag) != 4:
            tag = DEFAULT_TAG
            console.print("[yellow][WARN][/yellow] Tag must be four (4) characters!")
            console.print(f"[INFO] Using default tag {tag}")

        console.print(f"[INFO] Generating egghunter with tag {tag_to_hex(tag)} ({tag})")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = "Creates a 32-bit Windows assembly payload"
    )
    parser.add_argument(
        '--egghunter',
        help = "Generate a 32-bit SEH or NtAccess egghunter",
        action = 'store_true'
    )
    parser.add_argument(
        '--tag',
        help = f"Egghunter tag to use (default: {DEFAULT_TAG})"
    )

    main(parser.parse_args())
