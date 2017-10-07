from ....agent_factory.behaviors import *
from ....agent_factory.abstract_agent import *


class TimeOutAgent(AbstractAgent):

    class TimeOutAction(TimeOutBehaviour):

        def on_start(self):
            print("Starting behaviour . . .")

        def time_out_action(self):
            print("Hello, the timeout has ended!")

        def on_end(self):
            print("Ending behaviour . . .")

    def _setup(self):
        print(str(__class__.__name__) + " agent starting . . .")
        b = self.TimeOutAction(5)
        self.add_behaviour(b, None)
        b.start()
