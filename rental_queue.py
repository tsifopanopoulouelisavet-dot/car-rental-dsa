# Store one request and a link to the next request.
class RequestNode:
    def __init__(self, request):
        self.request = request
        self.next = None


# Manage rental requests in arrival order.
class RentalQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Add a request at the end of the queue.
    def enqueue(self, request):
        node = RequestNode(request)

        if self.rear is None:
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        # Remove and return the first request.
    def dequeue(self):
        if self.front is None:
            return None

        request = self.front.request
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return request

    # Check whether the queue is empty.
    def is_empty(self):
        return self.front is None    