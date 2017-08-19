from transitions import State, Machine

class Matter(object):
    def make_hissing_noises(self): print("HISSSSSSSSSSSSSSSS")
    def disappear(self): print("where'd all the liquid go?")

states=['solid', 'liquid', 'gas', 'plasma']

lump = Matter()
m = Machine(lump, states, before_state_change='make_hissing_noises', after_state_change='disappear')
lump.to_gas()