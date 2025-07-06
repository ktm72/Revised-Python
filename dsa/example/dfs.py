class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    """Add an item to the top of the stack."""
    self.items.append(item)

  def pop(self):
    """Remove and return the top item of the stack."""
    if self.is_empty():
      raise IndexError("Pop from empty stack")
    return self.items.pop()

  def is_empty(self):
    """Check if the stack is empty."""
    return len(self.items) == 0


def dfs(graph, start):
  """Perform DFS on a graph starting from the given node."""
  visited = set()  # Track visited nodes
  stack = Stack()  # Stack for DFS
  result = []  # Store the order of traversal

  # Start DFS from the given node
  stack.push(start)

  while not stack.is_empty():
    # Pop a node from the stack
    current = stack.pop()
    print("current", current)
    # If the node has not been visited, process it
    if current not in visited:
      visited.add(current)
      result.append(current)
      # run the function on the current node

      # Push all unvisited neighbors onto the stack
      for neighbor in reversed(graph[current]):  # Reverse to maintain order
        # print(f"visiting: {neighbor} from {current}")
        if neighbor not in visited:
          print(f"Newly visiting: {neighbor} from {current}")
          stack.push(neighbor)
  
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
  print(f"DFS traversal starting from {start_node}: {dfs(graph, start_node)}")