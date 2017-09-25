import os, sys, inspect

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
    
from transitions import *
from transitions.extensions import GraphMachine

class BetBase(object):
    
    # graph object is created by the machine
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('betBase.png', prog='dot')

states=['CreateBet','OpenBet','BetOn','CloseBet','Paying','UpdateLists']
transitions = [
    { 'trigger': 'Configure', 'source': 'CreateBet', 'dest': 'OpenBet' },
    { 'trigger': 'Public', 'source': 'OpenBet', 'dest': 'BetOn'},
    { 'trigger': 'FinishTime', 'source': 'BetOn', 'dest': 'CloseBet' },
    { 'trigger': 'ProcessPayment', 'source': 'CloseBet', 'dest': 'Paying' },
    { 'trigger': 'ProcessResults', 'source': 'Paying', 'dest': 'UpdateLists' }
]

model = BetBase()
machine = GraphMachine(model=model, 
                       states=states, 
                       transitions=transitions,
                       initial='BaseBet',
                       title="Bet",
                       show_conditions=True)
model.show_graph()

