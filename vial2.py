#!/usr/bin/python

import argparse
import sys
from rich.console import Console

bn = '''[green]
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
        tag = DEFAULT_TAG
    return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"

if __name__ == '__main__':

    console = Console()
    console.print(bn)

    try:
        key = sys.argv[1]
        console.log(f"Generating egghunter...")
        console.log(f"Using key: {tag_to_hex(key)}")
    except IndexError:
        sys.exit()