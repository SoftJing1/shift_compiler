import angr

# Load the binary
proj = angr.Project('../scompiler', load_debug_info=True)
proj.kb.dvars.load_from_dwarf()
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)

from utils import *