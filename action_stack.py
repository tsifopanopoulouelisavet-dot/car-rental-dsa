# Store actions so the latest action is removed first.
class ActionStack:
    def __init__(self):
        self.actions = []

    # Add an action to the top of the stack.
    def push(self, action):
        self.actions.append(action)

    # Remove and return the latest action.
    def pop(self):
        if self.is_empty():
            return None

        return self.actions.pop()

    # Check whether the stack is empty.
    def is_empty(self):
        return len(self.actions) == 0