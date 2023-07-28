#ifndef AST_HPP
#define AST_HPP

#include "tokens.hpp"
#include <string>

using namespace std;

namespace AST{

    struct AST_node{};

    enum variable_type{vINT, vVAR};

    struct Variable: AST_node{
        variable_type type;
        string value;

        Variable(variable_type t, string v): type(t), value(v){};
    };

    enum program_type{ pSHL, pMUL};

    struct Program: AST_node{
        program_type op;
        Variable v1;
        Variable v2;
        
        Program(program_type t, Variable V1, Variable V2): op(t), v1(V1), v2(V2){}
    };
}

AST::Program parse();

#endif