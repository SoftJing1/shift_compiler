#include "target.hpp"
#include <iostream>

using namespace std;

Target::Operand::Operand(const Target::Operand& o){
    type = o.type;
    switch(type){
        case Target::oINT:
            value = o.value;
            break;
        // case Target::oVAR:
        //     name = o.name;
        //     break;
        default:
            // cerr<<"Error: Target operand constructor: invalid operand type"<<endl;
            exit(1);
    }
}