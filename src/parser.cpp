#include "all.hpp"

using namespace std;

Program parse(){
    parse_program();
}

Program parse_program(){
    auto op = move(get_token());
    auto v1 = move(parse_variable());
    auto v2 = move(parse_variable());
    return Program(op, Variable(v1), Variable(v2));
};

Variable parse_variable(){
    auto tk = move(get_token());
    return Variable(tk);
};