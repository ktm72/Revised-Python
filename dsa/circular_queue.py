class CircularQueue:
    def __init__(self, capacity):
        """Initialize the circular queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity  # Fixed-size list to store elements
        self.front = -1  # Points to the front of the queue
        self.rear = -1  # Points to the rear of the queue

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0  # Set front to the first position if the queue is empty
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = item

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the dequeued position
        if self.front == self.rear:  # If the queue becomes empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity  # Circular increment
        return item

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[self.front]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Check if the queue is full."""
        return (self.rear + 1) % self.capacity == self.front

    def __repr__(self):
        """Return a string representation of the queue."""
        return str(self.queue)


# Example usage:
if __name__ == "__main__":
    capacity = 5
    circular_queue = CircularQueue(capacity)

    # Enqueue elements
    circular_queue.enqueue(1)
    circular_queue.enqueue(2)
    circular_queue.enqueue(3)
    circular_queue.enqueue(4)
    print("Queue after enqueuing 4 elements:", circular_queue)

    # Dequeue elements
    print("Dequeued:", circular_queue.dequeue())
    print("Queue after dequeuing 1 element:", circular_queue)

    # Enqueue more elements
    circular_queue.enqueue(5)
    circular_queue.enqueue(6)
    print("Queue after enqueuing 2 more elements:", circular_queue)

    # Peek at the front element
    print("Front element:", circular_queue.peek())

    # Check if the queue is full
    print("Is the queue full?", circular_queue.is_full())

    # Dequeue all elements
    while not circular_queue.is_empty():
        print("Dequeued:", circular_queue.dequeue())
    print("Queue after dequeuing all elements:", circular_queue)