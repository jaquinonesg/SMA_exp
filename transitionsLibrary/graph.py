from transitions import Machine, State
from transitions.extensions import GraphMachine as Machine

class Matter(object):
    pass

lump = Matter()


states = ['liquid','solid','gas','plasma']

transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid'},
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}
]

machine = Machine(lump, states=states, transitions=transitions, initial='solid')
# in cases where auto transitions should be visible
# Machine(model=m, show_auto_transitions=True, ...)

# draw the whole graph ...
m.get_graph().draw('my_state_diagram.png', prog='dot')
# ... or just the region of interest
# (previous state, active state and all reachable states)
m.get_graph(show_roi=True).draw('my_state_diagram.png', prog='dot')