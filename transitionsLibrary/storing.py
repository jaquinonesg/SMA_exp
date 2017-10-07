from transitionslib.core import State, Machine
import pickle

m = Machine(states=['A', 'B', 'C'], initial='A')
m.to_B()
print(m.state)

# store the machine
dump = pickle.dumps(m)

# load the Machine instance again
m2 = pickle.loads(dump)

print(m2.state)


print(m2.states.keys())
