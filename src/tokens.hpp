#ifndef TOKENS_HPP
#define TOKENS_HPP

#include <string>
using namespace std;

enum token_type{ tSHL, tMUL, tINT, tVAR,};

struct token{
    token_type type;
    string value;
};

#endif