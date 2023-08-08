# use clang to compile the src 

CC = clang++
CFLAGS = -std=c++11
SRCS = $(shell find ./src -name "*.cpp")
DEBUG = -g3 -O0 -fno-omit-frame-pointer 

all: scompiler

scompiler: $(SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o scompiler $(SRCS)

clean:
	rm -f scompiler
