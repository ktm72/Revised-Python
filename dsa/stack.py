class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    """Add an item to the top of the stack."""
    self.items.append(item)

  def pop(self):
    """Remove and return the top item of the stack. Raise an error if the stack is empty."""
    if self.is_empty():
      raise IndexError("Pop from empty stack")
    return self.items.pop()

  def peek(self):
    """Return the top item of the stack without removing it. Raise an error if the stack is empty."""
    if self.is_empty():
      raise IndexError("Peek from empty stack")
    return self.items[-1]

  def is_empty(self):
    """Check if the stack is empty."""
    return len(self.items) == 0

  def size(self):
    """Return the number of items in the stack."""
    return len(self.items)

# Example usage:
if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  print(stack.peek())  # Output: 3
  print(stack.pop())   # Output: 3
  print(stack.size())  # Output: 2
  print(stack.is_empty())  # Output: False
  stack.pop()
  stack.pop()
  print(stack.is_empty())  # Output: True