#include "all.hpp"
#include <map>

using namespace std;

AST::Program parse(){
    parse_program();
}

map<token_type, AST::program_type> op_map = {
    {tSHL, AST::pSHL},
    {tMUL, AST::pMUL},
};

AST::Program parse_program(){
    auto tk = move(get_token());
    auto op = op_map[tk.type];
    auto v1 = move(parse_variable());
    auto v2 = move(parse_variable());
    return AST::Program(op, AST::Variable(v1), AST::Variable(v2));
};

map<token_type, AST::variable_type> vtype_map = {
    {tINT, AST::vINT},
    {tVAR, AST::vVAR},
};

AST::Variable parse_variable(){
    auto tk = move(get_token());
    auto type = vtype_map[tk.type];
    return AST::Variable(type, tk.value);
};