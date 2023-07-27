#ifndef AST_HPP
#define AST_HPP

#include "tokens.hpp"

struct AST_node{};

struct Variable: AST_node{
    token tk;

    Variable(token TK): tk(TK){};
};

struct Program: AST_node{
    token op;
    Variable v1;
    Variable v2;
    
    Program(token T, Variable V1, Variable V2): op(T), v1(V1), v2(V2){}
};


#endif