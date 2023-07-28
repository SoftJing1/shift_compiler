# use clang to compile the src 

CC = g++
CFLAGS = -std=c++11

all: scompiler

scompiler: $(shell find ./src -name "*.cpp")
	$(CC) $(CFLAGS) -o scompiler $(shell find ./src -name "*.cpp")

clean:
	rm -f scompiler
