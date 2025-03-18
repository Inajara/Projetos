CFLAGS=-ffreestanding -O2 -Wall -Wextra
LDFLAGS=-T boot/linker.ld -nostdlib
AS=nasm
CC=i686-linux-gnu-gcc

all: kernel.bin

bootloader.bin: boot/bootloader.asm
	$(AS) -f bin boot/bootloader.asm -o bootloader.bin

kernel.bin: bootloader.bin kernel/kernel.c
	$(CC) $(CFLAGS) -c kernel/kernel.c -o kernel.o
	$(CC) $(LDFLAGS) kernel.o -o kernel.elf
	dd if=/dev/zero of=kernel.bin bs=512 count=2880
	dd if=bootloader.bin of=kernel.bin conv=notrunc
	dd if=kernel.elf of=kernel.bin seek=1 conv=notrunc

run:
	qemu-system-i386 -drive format=raw,file=kernel.bin

clean:
	rm -f *.o *.bin *.elf