#ifndef TARGET_HPP
#define TARGET_HPP

#include <string>

using namespace std;

struct Instruction{};

struct Shl: Instruction{
    string v1;
    string v2;
};

struct Mul: Instruction{
    string v1;
    string v2;
};

#endif