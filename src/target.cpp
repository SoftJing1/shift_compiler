#include "target.hpp"

using namespace std;

Target::Operand::Operand(const Target::Operand& o){
    auto type = o.type;
    switch(type){
        case Target::oINT:
            value = o.value;
            break;
        case Target::oVAR:
            name = o.name;
            break;
        default:
            throw "Error: invalid operand type";
    }
}