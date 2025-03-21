CC = gcc
CFLAGS = -Iinclude -Wall
LDFLAGS = -lSDL2
SRC = src/graphics.c
EXAMPLES = examples/main.c
OUT = bin/example

all:
	mkdir -p bin
	$(CC) $(CFLAGS) $(SRC) $(EXAMPLES) -o $(OUT) $(LDFLAGS)

clean:
	rm -rf bin/
