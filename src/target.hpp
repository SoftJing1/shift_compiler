#ifndef TARGET_HPP
#define TARGET_HPP

#include <map>
#include <string>
#include "ast.hpp"

using namespace std;

namespace Target{

    struct Instruction{};

    enum operand_type{oINT, oVAR};

    static map<AST::operand_type, operand_type> vtype_map = {
        {AST::oINT, oINT},
        {AST::oVAR, oVAR}
    };

    struct Operand: Instruction{
        operand_type type;
        union {
            int value;
            string name;
        };
        Operand(const Operand&);
        Operand(AST::Operand o): type(vtype_map[o.type]), value(o.value){};
        ~Operand(){};

        protected:
        Operand(operand_type t, string v): type(t), name(v){};
        Operand(operand_type t, int v): type(t), value(v){};
    };

    struct Variable: public Operand{
        Variable(string v): Operand(oVAR, v){};
    };

    struct Constant: public Operand{
        Constant(int v): Operand(oINT, v){};
    };

    enum result_type{ iSHL, iMUL};

    struct Result: Instruction{
        result_type type;
        Operand o1;
        Operand o2;
        Result(result_type t, Operand O1, Operand O2): type(t), o1(O1), o2(O2){};
    };

}

Target::Result generate(AST::Program p);
void code_output(Target::Result result);

#endif