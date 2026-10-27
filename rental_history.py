# Store one rental record and a link to the next record.
class RentalNode:
    def __init__(self, plate, customer, days):
        self.plate = plate
        self.customer = customer
        self.days = days
        self.next = None


# Manage rental records as a linked list.
class RentalHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a rental record at the end.
    def add(self, plate, customer, days):
        new_node = RentalNode(plate, customer, days)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Visit and display each rental record.
    def display(self):
        current = self.head

        if current is None:
            print("No rental records")
            return

        while current is not None:
            print(current.plate, current.customer, current.days)
            current = current.next