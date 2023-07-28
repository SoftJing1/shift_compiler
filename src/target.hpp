#ifndef TARGET_HPP
#define TARGET_HPP

#include <map>
#include <string>
#include "ast.hpp"

using namespace std;

namespace Target{

    struct Instruction{};

    enum variable_type{vINT, vVAR,};

    map<AST::variable_type, variable_type> vtype_map = {
        {AST::vINT, vINT},
        {AST::vVAR, vVAR},
    };

    struct Variable: Instruction{
        variable_type type;
        string value;
        Variable(variable_type t, string v): type(t), value(v){};
        Variable(AST::Variable v): type(vtype_map[v.type]), value(v.value){};
    };

    enum result_type{ iSHL, iMUL,};

    struct Result: Instruction{
        result_type type;
        Variable v1;
        Variable v2;
        Result(result_type t, Variable V1, Variable V2): type(t), v1(V1), v2(V2){};
    };

}

Target::Result generate(AST::Program p);
void output(Target::Result result);

#endif