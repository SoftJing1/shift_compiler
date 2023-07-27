#include "all.hpp"

using namespace std;

token_type get_token_type(string tk){
    if(tk == "SHL") return SHL;
    if(tk == "MUL") return MUL;
    if(tk.find_first_not_of("0123456789") == string::npos) return INT;
    if(tk.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos) return VAR;
}

token get_token(){
    string tk;
    program >> tk;
    return {get_token_type(tk), tk};
}