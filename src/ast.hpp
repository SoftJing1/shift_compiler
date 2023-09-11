#ifndef AST_HPP
#define AST_HPP

#include "tokens.hpp"
#include <string>

using namespace std;

namespace AST{

    struct AST_node{};

    enum operand_type{oINT, oVAR};

    struct Operand: AST_node{
        operand_type type;
        int value;
        Operand(const Operand&);
        ~Operand(){};

        Operand(int c): type(oINT), value(c){};
        // Operand(string s): type(oVAR), name(s){};
    };

    using Variable = Operand;
    using Constant = Operand;

    enum program_type{ pSHL, pMUL};

    struct Program: AST_node{
        program_type op;
        Operand o1;
        Operand o2;
        
        Program(program_type t, Operand O1, Operand O2): op(t), o1(O1), o2(O2){}
    };
}

AST::Program parse();

#endif