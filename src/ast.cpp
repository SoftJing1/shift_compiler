#include "ast.hpp"

using namespace std;

AST::Operand::Operand(const AST::Operand& o){
    auto type = o.type;
    switch(type){
        case AST::oINT:
            value = o.value;
            break;
        case AST::oVAR:
            name = o.name;
            break;
        default:
            throw "Error: invalid operand type";
    }
}