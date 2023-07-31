#include <string>
#include "ast.hpp"
#include "target.hpp"

using namespace std;

string semantics(AST::Program p);
string semantics(Target::Result r);