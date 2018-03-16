def generate_state_machine(text):
    states=list(text)
    transitions = []
    i = 0
    while (i<len(states)-1):
        trigger = states[i]+"to"+states[i+1]
        transition = { 'dest':states[i+1], 'source':states[i], 'trigger':trigger}
        transitions.append(transition)
        i += 1