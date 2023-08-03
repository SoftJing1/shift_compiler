# use clang to compile the src 

CC = g++
CFLAGS = -std=c++11
SRCS = $(shell find ./src -name "*.cpp")
DEBUG = -g3 -O0

all: scompiler

scompiler: $(SRCS)
	$(CC) $(CFLAGS) -o scompiler $(SRCS)

debug: $(SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o scompiler $(SRCS)

clean:
	rm -f scompiler
