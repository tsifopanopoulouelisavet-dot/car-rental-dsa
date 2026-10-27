from rental_queue import RentalQueue

# Check an empty queue.
queue = RentalQueue()
assert queue.is_empty() is True
assert queue.dequeue() is None

# Check that requests come out in arrival order.
queue.enqueue("Anna")
queue.enqueue("Nikos")

assert queue.is_empty() is False
assert queue.dequeue() == "Anna"
assert queue.dequeue() == "Nikos"

# Check that both pointers reset when the queue is empty.
assert queue.is_empty() is True
assert queue.front is None
assert queue.rear is None
assert queue.dequeue() is None

# Check that the queue can be reused.
queue.enqueue("Maria")
assert queue.dequeue() == "Maria"
assert queue.is_empty() is True

print("Rental Queue tests: PASS")