class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
        return None
    return self.items.pop()

  def peek(self):
      if self.is_empty():
          return None
      return self.items[-1]

  def is_empty(self):
      return len(self.items) == 0

def is_balanced_brackets(string):
  """Check if the brackets in the string are balanced."""
  stack = Stack()
  # Dictionary to map closing brackets to their corresponding opening brackets
  bracket_map = {')': '(', '}': '{', ']': '['}

  for char in string:
    if char in '({[':  # If it's an opening bracket, push it onto the stack
      stack.push(char)
    elif char in ')}]':  # If it's a closing bracket
      # Check if the stack is empty or the top of the stack doesn't match
      if stack.is_empty() or stack.pop() != bracket_map[char]:
        return False

  # If the stack is empty, all brackets were matched
  return stack.is_empty()


# Example usage:
if __name__ == "__main__":
  test_strings = [
    "()",  # Balanced
    "([])",  # Balanced
    "{[()]}",  # Balanced
    "{[(])}",  # Not Balanced
    "((()))",  # Balanced
    "(()",  # Not Balanced
  ]

  for s in test_strings:
    print(f"{s}: {'Balanced' if is_balanced_brackets(s) else 'Not Balanced'}")