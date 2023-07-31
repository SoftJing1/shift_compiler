#include "ast.hpp"
#include <fstream>

using namespace std;

extern istream program;

token_type get_token_type(string tk){
    if(tk == "SHL" || tk == "shl") return tSHL;
    if(tk == "MUL" || tk == "mul") return tMUL;
    if(tk.find_first_not_of("0123456789") == string::npos) return tINT;
    if(tk.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos) return tVAR;
    throw "Error: invalid token";
}

token get_token(){
    string tk;
    program >> tk;
    return {get_token_type(tk), tk};
}