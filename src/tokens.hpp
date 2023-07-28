#ifndef TOKENS_HPP
#define TOKENS_HPP

#include <string>
using namespace std;

enum token_type{ tSHL, tMUL, tINT, tVAR, tUNKNOWN};

struct token{
    token_type type;
    string value;
};

token get_token();

#endif