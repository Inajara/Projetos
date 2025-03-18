CC = gcc
CFLAGS = -Wall -Wextra
SRC = src/main.c src/ia.c src/utils.c
OUT = build/projeto_IA

all:
	mkdir -p build
	$(CC) $(CFLAGS) $(SRC) -o $(OUT)

run: all
	./$(OUT)

clean:
	rm -rf build
