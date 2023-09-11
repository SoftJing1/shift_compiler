#include "ast.hpp"
#include <iostream>

using namespace std;

AST::Operand::Operand(const AST::Operand& o){
    type = o.type;
    switch(type){
        case AST::oINT:
            value = o.value;
            break;
        // case AST::oVAR:
        //     name = o.name;
        //     break;
        default:
            // cerr<<"Error: AST operand constructor: invalid AST operand type"<<endl;
            exit(1);
    }
}