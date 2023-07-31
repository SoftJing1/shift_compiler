/*
    Semantics is the same language spoken by both source language and target language.
    For simplicity, we will use plain string as the semantics of both languages.
*/

#include "ast.hpp"
#include "target.hpp"
#include <string>

using namespace std;

string semantics(AST::Program p){
    switch(p.op){
        case AST::pSHL:
            return p.v1.value + " << " + p.v2.value;
        case AST::pMUL:
            return p.v1.value + " * " + p.v2.value;
    }
    exit(1);
}

string semantics(Target::Result r){
    switch(r.type){
        case Target::iSHL:
            return r.v1.value + " << " + r.v2.value;
        case Target::iMUL:
            return r.v1.value + " * " + r.v2.value;
    }
    exit(1);
}
