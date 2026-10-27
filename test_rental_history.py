from rental_history import RentalHistory

# Check that a new rental history is empty.
history = RentalHistory()

assert history.head is None
assert history.tail is None

# Check the first rental record.
history.add("ABC-123", "Anna", 3)

assert history.head is history.tail
assert history.head.plate == "ABC-123"
assert history.head.customer == "Anna"
assert history.head.days == 3
assert history.head.next is None

print("Empty and first record tests: PASS")
# Check that new records are linked in the correct order.
first = history.head
history.add("DEF-456", "Nikos", 5)
history.add("GHI-789", "Maria", 2)

second = first.next
third = second.next

assert history.head is first
assert second.plate == "DEF-456"
assert second.customer == "Nikos"
assert second.days == 5
assert third.plate == "GHI-789"
assert third.customer == "Maria"
assert third.days == 2
assert history.tail is third
assert third.next is None

print("Multiple records tests: PASS")
from contextlib import redirect_stdout
from io import StringIO

# Capture and check the displayed rental records.
output = StringIO()
with redirect_stdout(output):
    history.display()

assert output.getvalue().splitlines() == [
    "ABC-123 Anna 3",
    "DEF-456 Nikos 5",
    "GHI-789 Maria 2",
]

# Check the message for an empty history.
output = StringIO()
with redirect_stdout(output):
    RentalHistory().display()

assert output.getvalue().strip() == "No rental records"

print("Display tests: PASS")