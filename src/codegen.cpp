#include <iostream>
#include "ast.hpp"
#include "target.hpp"

using namespace std;

// convert mul to shl if possible
Target::Result reduced(Target::Result r){
    if(r.type == Target::iMUL && r.v2.type == Target::vINT){
        int v2 = stoi(r.v2.value);
        // if v2 is power of 2
        if((v2 & (v2 - 1)) == 0){
            int i = 0;
            while(v2 >>= 1) i++;
            return {Target::iSHL, r.v1, {Target::vINT, to_string(i)}};
        }
    }
    return r;
}

Target::Result generate(AST::Program p){
    switch(p.op){
        case AST::pSHL:
            return {Target::iSHL, {p.v1}, {p.v2}};
        case AST::pMUL:
            return reduced({Target::iMUL, {p.v1}, {p.v2}});
    }
    exit(1);
}

void output(Target:: Result result){
    switch(result.type){
        case Target::iSHL:
            cout << "SHL " << result.v1.value << " " << result.v2.value << endl;
            break;
        case Target::iMUL:
            cout << "MUL " << result.v1.value << " " << result.v2.value << endl;
            break;
    }
}