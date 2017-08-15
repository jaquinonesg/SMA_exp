from transitions import Machine, State

class Matter(object):
    def say_hello(self): print("hello, new state!")
    def say_goodbye(self): print("goodbye, old state!")
    def on_enter_A(self): print("We've just entered state A!")
    def on_enter_B(self): print("We've just entered state B!")

lump = Matter()
transitions = [
    { 'trigger': 'passA', 'source': 'A', 'dest': 'B' },
    { 'trigger': 'passB', 'source': 'B', 'dest': 'C' },
    { 'trigger': 'passC', 'source': 'C', 'dest': 'A' }
]

machine = Machine(lump, states=['A', 'B', 'C'], transitions=transitions, initial='A')

lump.state
lump.passA()