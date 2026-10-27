from action_stack import ActionStack

# Check an empty stack.
stack = ActionStack()
assert stack.is_empty() is True
assert stack.pop() is None

# Check that the latest action comes out first.
stack.push("Rent ABC-123")
stack.push("Return DEF-456")

assert stack.is_empty() is False
assert stack.pop() == "Return DEF-456"
assert stack.pop() == "Rent ABC-123"

# Check that the stack is empty again.
assert stack.is_empty() is True
assert stack.pop() is None

print("Action Stack tests: PASS")