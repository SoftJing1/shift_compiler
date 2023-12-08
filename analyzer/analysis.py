import angr
import sys
import re
from utils import *
from angr.storage.memory_mixins.default_filler_mixin import uncon_vars

# Load the binary
proj = angr.Project(sys.argv[1], load_debug_info=True)
proj.kb.dvars.load_from_dwarf()
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)

# type that simulate the program struct in scompiler
arg_type = angr.types.parse_type('struct p {int type; struct {int type; int value;} x; struct {int type; int value;}y; }')
angr.types.register_types(arg_type)
func_prototype = 'struct p a(struct p b)'

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

addr = get_addr(proj, 'codegen', 8)
ca = proj.factory.callable(addr, prototype=func_prototype)
ca.perform_call(sym_input)

# manually map memory address to input variable
inputs = []
for var in uncon_vars:
    is_input = (
        var.size() == 32
        and re.match(r'mem_f.*', var._encoded_name.decode('ascii'))
    )
    if is_input: inputs.append(var)

    
# verification for: 
#       if input is SHL * *, then output will not be MUL * *
in_r_type, in_r_o2_type, in_r_o2_value, in_r_o1_type, in_r_o1_value = inputs
input_constraints = [in_r_type == 0]     # input is SHL * *  

for state in ca.result_path_group.active:
    output = state.mem[state.regs.rax].struct.p
    
    out_r_type = output.type
    out_r_o1_type = output.x.type
    out_r_o1_value = output.x.value
    out_r_o2_type = output.y.type
    out_r_o2_value = output.y.value
    
    neg_output_constraints = [out_r_type == 1]  # output is MUL * *
    
    if state.solver.satisfiable(input_constraints + neg_output_constraints):
        # assertion violated
        state.solver.add(input_constraints + neg_output_constraints)
        counter_example = [
            state.solver.eval(in_r_type),
            state.solver.eval(in_r_o1_type),
            state.solver.eval(in_r_o1_value),
            state.solver.eval(in_r_o2_type),
            state.solver.eval(in_r_o2_value)
        ]
        print('violation detected:', counter_example)

print('verification done, not bug found')
