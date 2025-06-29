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

  def __repr__(self):
      return str(list(self.items))


def reverse_first_k_elements(queue, k):
  """Reverse the first k elements of the queue."""
  if k > queue.size() or k <= 0:
    raise ValueError("Invalid value of k")

  stack = []  # Temporary stack to reverse the first k elements

  # Step 1: Dequeue the first k elements and push them onto the stack
  for _ in range(k):
    stack.append(queue.dequeue())

  # Step 2: Pop elements from the stack and enqueue them back to the queue
  while stack:
    queue.enqueue(stack.pop())

  # Step 3: Move the remaining elements in the queue to the back
  for _ in range(queue.size() - k):
    queue.enqueue(queue.dequeue())


# Example usage:
if __name__ == "__main__":
  queue = Queue()
  for i in range(1, 6):  # Enqueue elements 1, 2, 3, 4, 5
    queue.enqueue(i)

  print("Original Queue:", queue)
  k = 3
  reverse_first_k_elements(queue, k)
  print(f"Queue after reversing first {k} elements:", queue)