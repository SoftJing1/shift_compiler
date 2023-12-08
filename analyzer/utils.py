def line_info(proj, keyword = None):
    '''
    This function is used to print the line number of each address in the binary
    Example:
        line_info()
        line_info('main.cpp')
    '''
    line_map = proj.loader.main_object.addr_to_line
    for addr, line in line_map.items():
        if keyword == None: print(line, addr)
        else:
            keyword = str(keyword)
            for t in line:
                if keyword in t[0] or keyword == str(addr):
                    print(line, addr)

def get_addr(proj, target_file:str = None, target_line:int = None) -> int:
    '''
    get address based on the file name and line number
    '''
    if target_file is None or target_line is None: line_info()
    
    line_map = proj.loader.main_object.addr_to_line
    for addr, info in line_map.items():
        if info is None: continue
        
        for file_name, line_number in info:
            if target_file in file_name and line_number == target_line:
                return addr

def get_variables(proj):
    '''
    This function is used to print all variables loaded from DWARF
    '''
    dvars = proj.kb.dvars
    res = []
    for name, obj in dvars._dvar_containers.items():
        res.append(name)
    return res

def variable_visibility(proj, var_name):
    '''
    print all pc ranges in which the variable is visible
    '''
    for i in proj.kb.dvars[var_name].less_visible_vars: 
        print(i.low_pc, i.high_pc)

'''
get returned value of some state, not tested
'''
from angr import SimState
from angr.callable import SimCC, Callable
def get_return_val(ca:Callable, args, state:SimState):
    prototype = SimCC.guess_prototype([args], ca._func_ty).with_arch(ca._project.arch)
    if state is not None and prototype.returnty is not None:
        loc = ca._cc.return_val(prototype.returnty)
        val = loc.get_value(state, stack_base=state.regs.sp - ca._cc.STACKARG_SP_DIFF)
        return state.solver.simplify(val)
    else:
        return None