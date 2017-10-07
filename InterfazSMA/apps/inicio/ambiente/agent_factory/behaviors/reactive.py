from ...agent_factory.abstract_behavior import AbstractBehaviour
from transitions import *
from transitions.extensions import GraphMachine
import threading


#####################################################################

class Reactive(AbstractBehaviour):
    pass

#####################################################################


class FsmBehavior(AbstractBehaviour):

    def __init__(self, states=[], transitions=[], initial='', title="", graph=False):
        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.my_owner = None
        self._force_kill = threading.Event()
        self._exit_code = 0
        self._states = states
        self._transitions = transitions
        if  not graph:
            self._Fsm = Machine(model=self, states=states, transitions=transitions, initial=initial)
        else:
            self._Fsm = GraphMachine(model=self, states=states, transitions=transitions, initial=initial, title=title, show_conditions=True)
