import logging
from transitions import logger, Machine, States

logger.setLevel(logging.INFO)

states = ['liquid','solid','gas','plasma']

transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid'},
    {'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas'},
    {'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma'}
]

# Business as usual
machine = Machine(states=states, transitions=transitions, initial='solid')