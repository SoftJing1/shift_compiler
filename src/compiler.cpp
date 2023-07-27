#include "all.hpp"
#include <iostream>

using namespace std;

void main(int argc, char** argv){
    if(argc < 2){
        cout << "Usage: " << argv[0] << " <file>" << endl;
        return;
    }    
    program.open(argv[1]);
}