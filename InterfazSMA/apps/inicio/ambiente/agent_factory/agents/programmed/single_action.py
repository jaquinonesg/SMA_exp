from ....agent_factory.abstract_agent import *
from ....agent_factory.behaviors import *


class SingleActionAgent(AbstractAgent):

    class AnAction(OneShotBehavior):
        def on_start(self):
            print("Starting behaviour . . .")

        def _single_action(self):
            print('I am a single action agent!')

        def on_end(self):
            print("Ending behaviour . . .")

    def _setup(self):
        print(str(__class__.__name__) + "agent starting . . .")
        b = self.AnAction()
        self.add_behaviour(b, None)
        b.start()
