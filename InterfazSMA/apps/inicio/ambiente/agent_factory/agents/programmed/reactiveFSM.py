from ....agent_factory.abstract_agent import *
from ....agent_factory.behaviors import *


class ReactiveFsm(AbstractAgent):

    states = []
    transitions = []
    fsm = Machine()

    class FiniteStateMachine(FsmBehavior):
        def on_start(self):
            print("Starting behaviour . . .")

        def on_end(self):
            print("Ending behaviour . . .")

    def _setup(self):
        print(str(__class__.__name__) + " agent starting . . .")

        self.states = ['a','b','c','d']
        self.transitions = [
            { 'trigger': 'at', 'source': 'a', 'dest': 'b' },
            { 'trigger': 'bt', 'source': 'b', 'dest': 'c' },
            { 'trigger': 'ct', 'source': 'c', 'dest': 'd' },
            { 'trigger': 'dt', 'source': 'd', 'dest': 'a' },
        ]

        self.fsm = self.FiniteStateMachine(states=self.states, transitions=self.transitions, initial=self.states[0])
        self.add_behaviour(self.fsm, None)

        #b.start()
