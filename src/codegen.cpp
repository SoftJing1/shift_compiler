// #include <iostream>
#include "ast.hpp"
#include "target.hpp"
#include <bitset>
#include <iostream>

using namespace std;

// convert mul to shl if possible
Target::Result reduced(Target::Result r){
    if(r.type == Target::iMUL && r.o2.type == Target::oINT){
        // if v2 is power of 2
        if((r.o2.value & (r.o2.value - 1)) == 0){
            int i = 0;
            while(r.o2.value >>= 1) i++;
            return {Target::iSHL, r.o1, Target::Constant(i)};
        }
    }
    return r;
}

Target::Result generate(AST::Program p){
    Target::Result target;
    cout<<
    "(declare-const p_o1 (_ BitVec 32))\n"
    "(declare-const p_o2 (_ BitVec 32))\n"
    "(declare-const i_o1 (_ BitVec 32))\n"
    "(declare-const i_o2 (_ BitVec 32))\n";

    switch(p.op){
        case AST::pSHL:
            target = Target::Result(Target::iSHL, {p.o1}, {p.o2});
            cout<<
            "(assert (! (= p_o1 #b"<<bitset<32>(p.o1.value)<<") :named p_o1_init))\n"
            "(assert (! (= p_o2 #b"<<bitset<32>(p.o2.value)<<") :named p_o2_init))\n"
            "(assert (! (= i_o1 #b"<<bitset<32>(target.o1.value)<<") :named i_o1_init))\n"
            "(assert (! (= i_o2 #b"<<bitset<32>(target.o2.value)<<") :named i_o2_init))\n"
            "(assert (or \n"
            "   (not (! (= p_o1 i_o1) :named o1_equation))\n"
            "   (not (! (= p_o2 i_o2) :named o2_equation))\n"
            "   (not (! (= (bvshl p_o1 p_o2) (bvshl i_o1 i_o2)) :named semantic_eq))))\n"
            "(check-sat)\n";
            return target;
        case AST::pMUL:
            target = reduced({Target::iMUL, {p.o1}, {p.o2}});
            cout<<
            "(assert (! (= p_o1 #b"<<bitset<32>(p.o1.value)<<") :named p_o1_init))\n"
            "(assert (! (= p_o2 #b"<<bitset<32>(p.o2.value)<<") :named p_o2_init))\n"
            "(assert (! (= i_o1 #b"<<bitset<32>(target.o1.value)<<") :named i_o1_init))\n"
            "(assert (! (= i_o2 #b"<<bitset<32>(target.o2.value)<<") :named i_o2_init))\n"
            "(assert (or\n"
            "   (not (! (= (bvshl #b00000000000000000000000000000001 i_o2) p_o2) :named log))\n"
            "   (not (! (= (bvmul p_o1 p_o2) (bvshl i_o1 i_o2)) :named semantic_eq))))\n"
            "(check-sat)\n";
            return target;
        default:
            // cerr<<"Error: target generate: invalid AST to generate target"<<endl;
            exit(1);
    }
}

void code_output(Target:: Result result){
    switch(result.type){
        case Target::iSHL:
            cout << "SHL " << result.o1.value << " " << result.o2.value << endl;
            break;
        case Target::iMUL:
            cout << "MUL " << result.o1.value << " " << result.o2.value << endl;
            break;
        default:
            cerr<<"Error: code output: invalid instruction to output"<<endl;
            exit(1);
    }
}
