#ifndef TARGET_HPP
#define TARGET_HPP

#include <map>
#include <string>
#include "ast.hpp"

using namespace std;

namespace Target{

    struct Instruction{};

    enum operand_type{oINT, oVAR};

    static map<AST::operand_type, operand_type> otype_map = {
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
        Operand(AST::Operand& o): type(otype_map.at(o.type)), value(o.value){};
        Operand(string v): type(oVAR), name(v){};
        Operand(int v): type(oINT), value(v){};
        ~Operand(){};
    };

    using Constant = Operand;
    using Variable = Operand;

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