#ifndef TOKENS_HPP
#define TOKENS_HPP

#include <string>
using namespace std;

enum token_type{ SHL, MUL, INT, VAR,};

struct token{
    token_type type;
    string value;
};

#endif