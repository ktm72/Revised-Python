from collections import deque

class Queue:
  def __init__(self):
    self.items = deque()

  def enqueue(self, item):
    """Add an item to the end of the queue."""
    self.items.append(item)

  def dequeue(self):
    """Remove and return the item from the front of the queue."""
    if self.is_empty():
      raise IndexError("Dequeue from empty queue")
    return self.items.popleft()

  def is_empty(self):
    """Check if the queue is empty."""
    return len(self.items) == 0


def bfs(graph, start):
  """Perform BFS on a graph starting from the given node."""
  visited = set()  # Track visited nodes
  queue = Queue()  # Queue for BFS
  result = []  # Store the order of traversal

  # Start BFS from the given node
  queue.enqueue(start)
  visited.add(start)

  while not queue.is_empty():
    # Dequeue a node and process it
    current = queue.dequeue()
    result.append(current)
    print("current", current)
    # run the function on the current node

    # Enqueue all unvisited neighbors
    for neighbor in graph[current]:
        # print(f"visiting: {neighbor} from {current}")
      if neighbor not in visited:
        print(f"Newly visiting: {neighbor} from {current}")
        queue.enqueue(neighbor)
        visited.add(neighbor)
  return result


# Example usage:
if __name__ == "__main__":
  # Graph represented as an adjacency list
  graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
  }

  start_node = 'A'
  print(f"BFS traversal starting from {start_node}: {bfs(graph, start_node)}")