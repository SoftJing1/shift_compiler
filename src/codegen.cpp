#include <iostream>
#include "ast.hpp"

using namespace std;

void generate_codes(Program p){
    cout << "Generating codes..." << endl;
    cout << "Program: " << p.op.tk << " " << p.v1.tk << " " << p.v2.tk << endl;
    cout << "Codes generated!" << endl;
}