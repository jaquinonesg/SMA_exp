from transitionslib.core import Machine, State

class Matter(object):
    def raise_error(self, event): raise ValueError("Oh no")
    def prepare(self, event): print("I am ready!")
    def finalize(self, event): print("Result: ", type(event.error), event.error)

states=['solid', 'liquid', 'gas', 'plasma']

lump = Matter()
m = Machine(lump, states, prepare_event='prepare', before_state_change='raise_error',
            finalize_event='finalize', send_event=True)
try:
    lump.to_gas()
except ValueError:
    pass
print(lump.state)