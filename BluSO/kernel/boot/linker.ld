OUTPUT_FORMAT(elf32-i386)
ENTRY(start)

SECTIONS {
    . = 1M; /* Carregar o kernel a partir de 1MB na RAM */

    .text : {
        *(.multiboot)
        *(.text)
    }

    .data : { *(.data) }
    .bss : { *(.bss) }
}
