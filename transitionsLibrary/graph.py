from transitions.extensions import GraphMachine as Machine

class Matter(Machine):
    def say_hello(self): print("hello, new state!")
    def say_goodbye(self): print("goodbye, old state!")

    def __init__(self):
        states=['solid', 'liquid', 'gas', 'plasma']
        
        Machine.__init__(self, states=states, initial='solid')
        self.add_transition('melt', 'solid', 'liquid')
        self.add_transition('evaporate', 'liquid', 'gas')
        self.add_transition('sublimate', 'solid', 'gas')
        self.add_transition('ionize', 'gas', 'plasma')


lump = Matter()

# in cases where auto transitions should be visible
# Machine(model=m, show_auto_transitions=True, ...)

# draw the whole graph ...
lump.get_graph().draw('my_state_diagram.png', prog='dot')
# ... or just the region of interest
# (previous state, active state and all reachable states)
lump.get_graph(show_roi=True).draw('my_state_diagram.png', prog='dot')