#!/usr/bin/python

import sys

def to_hex(s):
    return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in s][::-1])}"

if __name__ == '__main__':
    try:
        key = sys.argv[1]
        print(to_hex(key))
    except IndexError:
        sys.exit()