class Matter(object):
    pass

lump = Matter()

from transitions import Machine
# The states
states=['solid', 'liquid', 'gas', 'plasma']

# And some transitions between states. We're lazy, so we'll leave out
# the inverse phase transitions (freezing, condensation, etc.).
transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
]
machine = Machine(lump, states=states, transitions=transitions, initial='liquid')

# Lump now has state!
print(lump.state)
lump.evaporate()
print(lump.state)
