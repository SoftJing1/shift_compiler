# use clang to compile the src 

CC = g++
CFLAGS = -std=c++11
SRCS = $(shell find ./src -name "*.cpp")
MIN_SRCS = $(shell find ./min_src -name "*.cpp")
DEBUG = -g -O0 

all: scompiler

scompiler: $(SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o scompiler $(SRCS)

min: $(MIN_SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o scompiler $(MIN_SRCS)

clean:
	rm -f scompiler
