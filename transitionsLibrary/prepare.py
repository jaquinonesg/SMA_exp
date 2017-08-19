from transitions import State, Machine
import random
class Matter(object):
    heat = False
    attempts = 0
    def count_attempts(self): self.attempts += 1
    def is_really_hot(self): return self.heat
    def heat_up(self): self.heat = random.random() < 0.25
    def stats(self): print('It took you %i attempts to melt the lump!' %self.attempts)

states=['solid', 'liquid', 'gas', 'plasma']

transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'prepare': ['heat_up', 'count_attempts'], 'conditions': 'is_really_hot', 'after': 'stats'},
]

lump = Matter()
machine = Machine(lump, states, transitions=transitions, initial='solid')
lump.melt()
