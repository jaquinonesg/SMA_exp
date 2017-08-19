def thing_a(arg=None):
    print ('thing_a', arg)

def thing_b(arg=None):
    print ('thing_b', arg)

ghetto_switch_statement = {
    'do_thing_a': thing_a,
    'do_thing_b': thing_b
}

ghetto_switch_statement['do_thing_a']("It's lovely being an A")
ghetto_switch_statement['do_thing_b']("Being a B isn't too shabby either")

print ("Available methods are: ", ghetto_switch_statement.keys())