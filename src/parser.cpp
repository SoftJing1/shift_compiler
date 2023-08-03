#include "ast.hpp"
#include <map>
#include <iostream>

using namespace std;

map<token_type, AST::operand_type> otype_map = {
    {tINT, AST::oINT},
    {tVAR, AST::oVAR}
};

AST::Operand parse_operand(){
    auto tk = get_token();
    auto type = otype_map.at(tk.type);

    switch(type){
        case AST::oINT:
            return AST::Constant(stoi(tk.value));
        case AST::oVAR:
            return AST::Variable(tk.value);
        default:
            cerr<<"Error: parse_operand: invalid operand type"<<endl;
            exit(1);
    }
};

map<token_type, AST::program_type> op_map = {
    {tSHL, AST::pSHL},
    {tMUL, AST::pMUL}
};

AST::Program parse_program(){
    auto tk = get_token();
    auto op = op_map.at(tk.type);
    auto o1 = parse_operand();
    auto o2 = parse_operand();

    return AST::Program(op, AST::Operand(o1), AST::Operand(o2));
};

AST::Program parse(){
    return parse_program();
}