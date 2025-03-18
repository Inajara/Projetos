[ORG 0x7C00]  ; Endereço onde o BIOS carrega o bootloader

mov si, msg
call print_string

jmp $

print_string:
    mov ah, 0x0E
.loop:
    lodsb
    cmp al, 0
    je .done
    int 0x10
    jmp .loop
.done:
    ret

msg db "Iniciando Kernel...", 0

times 510-($-$$) db 0
dw 0xAA55  ; Assinatura do setor de boot
