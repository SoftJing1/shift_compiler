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
        union {
            int value;
            string name;
        };
        Operand(const Operand&);
        ~Operand(){};

        protected:
        Operand(operand_type t, int c): type(t), value(c){};
        Operand(operand_type t, string s): type(t), name(s){};
    };

    struct Variable: public Operand{
        Variable(string v): Operand(oVAR, v){};
    };

    struct Constant: public Operand{
        Constant(int v): Operand(oINT, v){};
    };

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