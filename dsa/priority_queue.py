import heapq

class PriorityQueue:
  def __init__(self):
    self.heap = []  # Min-Heap to store elements with their priorities

  def enqueue(self, priority, item):
    """Add an item with a given priority to the priority queue."""
    heapq.heappush(self.heap, (priority, item))  # Push as a tuple (priority, item)

  def dequeue(self):
    """Remove and return the item with the highest priority (lowest value)."""
    if self.is_empty():
      raise IndexError("Dequeue from empty priority queue")
    return heapq.heappop(self.heap)[1]  # Pop the tuple and return the item

  def peek(self):
    """Return the item with the highest priority without removing it."""
    if self.is_empty():
      raise IndexError("Peek from empty priority queue")
    return self.heap[0][1]  # Return the item from the tuple at the root

  def is_empty(self):
    """Check if the priority queue is empty."""
    return len(self.heap) == 0

  def __repr__(self):
    """Return a string representation of the priority queue."""
    return str([item for priority, item in self.heap])


# Example usage:
if __name__ == "__main__":
  pq = PriorityQueue()

  # Enqueue elements with priorities
  pq.enqueue(3, "Task 3")
  pq.enqueue(1, "Task 1")
  pq.enqueue(4, "Task 4")
  pq.enqueue(2, "Task 2")

  print("Priority Queue after enqueues:", pq)
  print("Peek at highest priority:", pq.peek())
  print("Dequeued:", pq.dequeue())
  print("Priority Queue after dequeue:", pq)
  print("Dequeued:", pq.dequeue())
  print("Priority Queue after another dequeue:", pq)
