import os, sys, inspect

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
    
from transitions import *
from transitions.extensions import GraphMachine

class Fridge(object):
    
    # graph object is created by the machine
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('fridge.png', prog='dot')

transitions = [
    { 'trigger': 'high_temperature', 'source': 'turn_off', 'dest': 'turn_on' },
    { 'trigger': 'temperature_is_fine', 'source': 'turn_on', 'dest': 'turn_off'}
]
states=['turn_on','turn_off']

model = Fridge()
machine = GraphMachine(model=model, 
                       states=states, 
                       transitions=transitions,
                       initial='turn_off',
                       show_auto_transitions=True,
                       title="Fridge",
                       show_conditions=True)
model.show_graph()