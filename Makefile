# use clang to compile the src 

CC = g++
CFLAGS = -std=c++11
SRCS = $(shell find ./src -name "*.cpp")

all: scompiler

scompiler: $(SRCS)
	$(CC) $(CFLAGS) -o scompiler $(SRCS)

clean:
	rm -f scompiler
