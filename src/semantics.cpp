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

bool check(AST::Program p){
    auto result = generate(p);
    auto sa = semantics(p);
    auto si = semantics(result);
    
    if (sa == si){
        // cout<<"OK"<<endl;
        return true;
    }
    else{
        // cout<<"Error: semantics mismatch"<<endl;
        // cout<<"AST: "<<sa<<endl;
        // cout<<"Target: "<<si<<endl;
        return false;
    }
}