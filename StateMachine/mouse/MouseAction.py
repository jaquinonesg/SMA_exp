class MouseAction:
    def __init__(self,action):
        self.action = action
    def __str__(self):
        return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    def __hash__(self):
        return hash(self.action)

MouseAction.appears = MouseAction("mouse appears")
MouseAction.runsAway = MouseAction("mouse runs away")
MouseAction.appears = MouseAction("mouse enters trap")
MouseAction.appears = MouseAction("mouse escapes")
MouseAction.appears = MouseAction("mouse trapped")
MouseAction.appears = MouseAction("mouse removed")

    