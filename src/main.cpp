#include <iostream>
#include <fstream>
#include "ast.hpp"
#include "target.hpp"
#include "semantics.hpp"

using namespace std;

istream program(cin.rdbuf());

int main(int argc, char** argv){
    if(argc > 2){
        cout << "Usage: " << argv[0] << " [program_file]" << endl;
        exit(1);
    }
    if(argc == 2){
        fstream program_file;
        program_file.open(argv[1]);
        if(!program_file.is_open()){
            cout << "Error: " << argv[1] << " not found" << endl;
            exit(1);
        }
        program.rdbuf(program_file.rdbuf());
    }

    auto p = parse();
    auto result = generate(p);
    code_output(result);
    cout << semantics(p) << endl << semantics(result) << endl;

    return 1;
}