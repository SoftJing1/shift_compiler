from analysis import proj, simgr

# This function is used to print the line number of each address in the binary
def line_info(keyword = None):
    line_map = proj.loader.main_object.addr_to_line
    for addr, line in line_map.items():
        if keyword == None: print(line, addr)
        else:
            for t in line:
                if keyword in t[0]:
                    print(line, addr)