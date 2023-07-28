#include "all.hpp"
#include <iostream>

using namespace std;

int main(int argc, char** argv){
    if(argc < 2){
        cout << "Usage: " << argv[0] << " <file>" << endl;
        return 0;
    }    
    program.open(argv[1]);
    if(!program.is_open()){
        cout << "Error: " << argv[1] << " not found" << endl;
        return 0;
    }

    auto p = parse();
    auto result = generate(p);
    output(result);

    return 1;
}