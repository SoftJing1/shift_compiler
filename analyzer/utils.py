from analysis import proj, simgr

"""
This function is used to print the line number of each address in the binary
Example:
    line_info()
    line_info('main.cpp')
"""

def line_info(keyword = None):
    line_map = proj.loader.main_object.addr_to_line
    for addr, line in line_map.items():
        if keyword == None: print(line, addr)
        else:
            for t in line:
                if keyword in t[0] or keyword == str(addr):
                    print(line, addr)

"""
    This function is used to print all variables loaded from DWARF
"""
def get_variables():
    dvars = proj.kb.dvars
    for name, obj in dvars._dvar_containers.items():
        print(name)
