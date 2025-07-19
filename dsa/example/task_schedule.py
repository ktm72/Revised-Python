import heapq

class PriorityQueue:
  def __init__(self):
    self.heap = []

  def enqueue(self, priority, task):
    heapq.heappush(self.heap, (priority, task))

  def dequeue(self):
    if self.is_empty():
      raise IndexError("Dequeue from empty priority queue")
    return heapq.heappop(self.heap)[1]

  def is_empty(self):
    return len(self.heap) == 0


# Example usage:
if __name__ == "__main__":
  pq = PriorityQueue()

  # Enqueue tasks with priorities
  pq.enqueue(3, "Low priority task")
  pq.enqueue(1, "High priority task")
  pq.enqueue(2, "Medium priority task")

  print("Executing tasks based on priority:")
  while not pq.is_empty():
    print("Executing:", pq.dequeue())