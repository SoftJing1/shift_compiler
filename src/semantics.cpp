/*
    Semantics is the same language spoken by both source language and target language.
    For simplicity, we will use plain string as the semantics of both languages.
*/

#include "ast.hpp"
#include "target.hpp"
#include <string>
#include <iostream>

using namespace std;

string semantics(AST::Program p){
    switch(p.op){
        case AST::pSHL:
            return to_string(p.o1.value) + " << " + to_string(p.o2.value);
        case AST::pMUL:
            return to_string(p.o1.value) + " * " + to_string(p.o2.value);
        default:
            // cerr<<"Error: AST semantics: invalid AST"<<endl;
            exit(1);
    }
    exit(1);
}

string semantics(Target::Result r){
    switch(r.type){
        case Target::iSHL:
            return to_string(r.o1.value) + " << " + to_string(r.o2.value);
        case Target::iMUL:
            return to_string(r.o1.value) + " * " + to_string(r.o2.value);
        default:
            // cerr<<"Error: Target semantics: invalid instruction"<<endl;
            exit(1);
    }
    exit(1);
}

bool check(AST::Program p, Target::Result target){
    
    auto source_semantics = 0;
    auto target_semantics = 0;

    switch(p.op){
        case AST::pSHL:
            source_semantics = p.o1.value << p.o2.value;
            break;
        case AST::pMUL:
            source_semantics = p.o1.value * p.o2.value;
            break;
        default:
            // cerr<<"Error: AST check: invalid AST"<<endl;
            exit(1);
    }

    switch(target.type){
        case Target::iSHL:
            target_semantics = target.o1.value << target.o2.value;
            break;
        case Target::iMUL:
            target_semantics = target.o1.value * target.o2.value;
            break;
        default:
            // cerr<<"Error: Target check: invalid instruction"<<endl;
            exit(1);
    }

    if (source_semantics == target_semantics){
        return true;
    } else {
        return false;
    }
}