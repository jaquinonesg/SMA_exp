from ....agent_factory.behaviors import *
from ....agent_factory.abstract_agent import *


class CycleAgent(AbstractAgent):

    class Periodic(PeriodicBehaviour):

        def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        def _on_tick(self):
            print("Counter:", self.counter)
            self.counter = self.counter + 1

    def _setup(self):
        print(str(__class__.__name__)+" agent starting . . .")
        b = self.Periodic(1)
        self.add_behaviour(b, None)
        b.start()
