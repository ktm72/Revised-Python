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

  def peek(self):
    """Return the item at the front of the queue without removing it. Raise an error if the queue is empty."""
    if self.is_empty():
      raise IndexError("Peek from empty queue")
    return self.items[0]  # O(1)

  def is_empty(self):
    """Check if the queue is empty."""
    return len(self.items) == 0  # O(1)

  def size(self):
    """Return the number of items in the queue."""
    return len(self.items)  # O(1)

# Example usage:
if __name__ == "__main__":
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  print(queue.peek())  # Output: 1
  print(queue.dequeue())  # Output: 1
  print(queue.size())  # Output: 2
  print(queue.is_empty())  # Output: False
  queue.dequeue()
  queue.dequeue()
  print(queue.is_empty())  # Output: True