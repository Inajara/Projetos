// kernel/kernel.c
void kernel_main() {
    char *video_memory = (char *)0xB8000;
    *video_memory = 'K'; // Escreve 'K' na tela para indicar que o kernel foi carregado
}
