# use clang to compile the src 

CC = clang++
CFLAGS = -std=c++11 
DEBUG = -g 

SRCS = $(shell find ./src -name "*.cpp")
MIN_SRCS = $(shell find ./min_src -name "*.cpp")

all: scompiler

scompiler: $(SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o scompiler $(SRCS)

min: $(MIN_SRCS)
	$(CC) $(CFLAGS) $(DEBUG) -o min $(MIN_SRCS)

combine: $(SRCS)
	@for file in $(SRCS); do \
		cat $$file; \
		echo; \
	done > ./src/combine.cpp
	$(CC) $(CFLAGS) $(DEBUG) -o combine ./src/combine.cpp

clean:
	rm -f scompiler min combine
	rm -f ./src/combine.cpp
