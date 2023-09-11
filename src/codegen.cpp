#include <iostream>
#include "ast.hpp"
#include "target.hpp"

using namespace std;

// convert mul to shl if possible
Target::Result reduced(Target::Result r){
    if(r.type == Target::iMUL && r.o2.type == Target::oINT){
        int& v = r.o2.value;
        // if v2 is power of 2
        if((v & (v - 1)) == 0){
            int i = 0;
            // while(v >>= 1) i++;
            return {Target::iSHL, r.o1, Target::Constant(i)};
        }
    }
    return r;
}

Target::Result generate(AST::Program p){
    switch(p.op){
        case AST::pSHL:
            return {Target::iSHL, {p.o1}, {p.o2}};
        case AST::pMUL:
            return reduced({Target::iMUL, {p.o1}, {p.o2}});
        default:
            // cerr<<"Error: target generate: invalid AST to generate target"<<endl;
            exit(1);
    }
}

void code_output(Target:: Result result){
    switch(result.type){
        case Target::iSHL:
            // cout << "SHL " << result.o1.value << " " << result.o2.value << endl;
            break;
        case Target::iMUL:
            // cout << "MUL " << result.o1.value << " " << result.o2.value << endl;
            break;
        default:
            // cerr<<"Error: code output: invalid instruction to output"<<endl;
            exit(1);
    }
}