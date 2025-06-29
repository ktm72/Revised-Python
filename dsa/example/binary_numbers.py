from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)  # O(1)

    def dequeue(self):
        """Remove and return the item from the front of the queue. Raise an error if the queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()  # O(1)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0  # O(1)

    def __repr__(self):
        return str(list(self.items))


def generate_binary_numbers(n):
    """Generate binary numbers from 1 to n using a queue."""
    queue = Queue()
    result = []

    # Enqueue the first binary number
    queue.enqueue("1")

    for _ in range(n):
        # Dequeue the front binary number
        binary_number = queue.dequeue()
        result.append(binary_number)

        # Enqueue the next two binary numbers
        queue.enqueue(binary_number + "0")
        queue.enqueue(binary_number + "1")

    return result


# Example usage:
if __name__ == "__main__":
    n = 10  # Generate binary numbers from 1 to 10
    binary_numbers = generate_binary_numbers(n)
    print(f"Binary numbers from 1 to {n}: {binary_numbers}")