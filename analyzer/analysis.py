import angr
import sys
# Load the binary

proj = angr.Project(sys.argv[1], load_debug_info=True)
# proj.kb.dvars.load_from_dwarf()
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)

from utils import *

# type that simulate the program struct in scompiler
arg_type = angr.types.parse_type('struct p {int type; struct {int type; int value;} x; struct {int type; int value;}y; }')
angr.types.register_types(arg_type)
func_prototype = 'int a(struct p b, struct p c)'

# symbolic input, a represents instruction type, aka SHL or MUL
# b and d are operand type, aka INT or STR
# c and e are operand value
a = state.solver.BVS('a', 32)
b = state.solver.BVS('b', 32)
c = state.solver.BVS('c', 32)
d = state.solver.BVS('d', 32)
e = state.solver.BVS('e', 32)
sym_input = (a, (b, c), (d, e))
conc_input = (0, (0, 0), (0, 0))
