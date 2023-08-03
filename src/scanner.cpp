#include "ast.hpp"
#include <fstream>
#include <iostream>

using namespace std;

extern istream program;

token_type get_token_type(string tk){
    if(tk == "SHL" || tk == "shl") return tSHL;
    if(tk == "MUL" || tk == "mul") return tMUL;
    if(tk.find_first_not_of("0123456789") == string::npos) return tINT;
    if(tk.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos) return tVAR;

    cerr<<"Error: get token type: invalid token"<<endl;
    exit(1);
}

token get_token(){
    string tk;
    program >> tk;
    return {get_token_type(tk), tk};
}