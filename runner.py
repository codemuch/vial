import ctypes
import struct
import sys
from lib.core import Util

"""
    runner.py - shellcode runner

    Takes a NASM assembly file containing some shellcode, turns it into
    opcodes using Keystone Engine, and runs it using VirtualAlloc, RtlMoveMemory,
    and CreateThread from the Win32 API via ctypes.

    Will dump the resulting opcodes to the console, highlighting NULL bytes.

    Usage:
    python runner.py shellcode/filename.nasm
"""
if __name__ == '__main__':
    SHELLCODE_FILE = sys.argv[1];
    SHELLCODE = Util.read_nasm(SHELLCODE_FILE)

    encoding, count = Util.read_bytes(SHELLCODE)

    print(f"[INFO] Encoded {count} instructions ({len(encoding)} bytes)")
    Util.dump_nasm_bytes(encoding)

    sh = b""
    for e in encoding:
        sh += struct.pack("B", e)
    shellcode = bytearray(sh)

    ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                            ctypes.c_int(len(shellcode)),
                                            ctypes.c_int(0x3000),
                                            ctypes.c_int(0x40))

    buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                        buf,
                                        ctypes.c_int(len(shellcode)))

    print(f"\n[+] Shellcode located at address {hex(ptr)}")
    input("...PRESS ENTER TO EXECUTE SHELLCODE...")

    ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                            ctypes.c_int(0),
                                            ctypes.c_int(ptr),
                                            ctypes.c_int(0),
                                            ctypes.c_int(0),
                                            ctypes.pointer(ctypes.c_int(0)))

    ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))