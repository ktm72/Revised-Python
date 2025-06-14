class Node:
  def __init__(self):
    self.data = None
    self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def append(self, item):
    new_node = Node() # Create a new node
    new_node.data = item
    if not self.head:
      # If the list is empty, 
      # set head and tail to the same node
      self.head = new_node # access through reference
      self.tail = new_node # access through reference
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.size += 1

  def insert(self, index, item):
    if index < 0 or index > self.size:
      raise IndexError("Index out of bounds")
    new_node = Node()
    new_node.data = item
    if index == 0:
      new_node.next = self.head
      self.head = new_node
      if not self.tail:
        self.tail = new_node
    else:
      current = self.head
      for _ in range(index - 1):
        current = current.next
      new_node.next = current.next
      current.next = new_node
      if new_node.next is None:
        self.tail = new_node
    self.size += 1
    
  def remove(self, item):
    if not self.head:
      raise ValueError("Item not found")
    if self.head.data == item:
      self.head = self.head.next
      if not self.head:
        self.tail = None
      self.size -= 1
      return
    current = self.head
    while current.next and current.next.data != item:
      current = current.next
    if current.next is None:
      raise ValueError("Item not found")
    current.next = current.next.next
    if current.next is None:
      self.tail = current
    self.size -= 1

  def pop(self):
    if not self.head:
      raise IndexError("Couldn't pop out from empty list")
    item = self.tail.data
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      current = self.head
      while current.next != self.tail:
        current = current.next
      current.next = None
      self.tail = current
    self.size -= 1
    return item
  def __getitem__(self, index):
    if index < 0 or index >= self.size:
      raise IndexError("Index out of bounds")
    current = self.head
    for _ in range(index):
      current = current.next
    return current.data
  def __setitem__(self, index, value):
    if index < 0 or index >= self.size:
      raise IndexError("Index out of bounds")
    current = self.head
    for _ in range(index):
      current = current.next
    current.data = value
  def __str__(self):
    elements = []
    current = self.head
    while current:
      elements.append(str(current.data))
      current = current.next
    return " -> ".join(elements) if elements else "Empty List"

  def __repr__(self):
    return f"SinglyLinkedList([{', '.join(repr(item) for item in self)})])"
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0
  def index(self, item):
    current = self.head
    index = 0
    while current:
      if current.data == item:
        return index
      current = current.next
      index += 1
    raise ValueError("Item not found in the list")
  def reverse(self):
    prev = None
    current = self.head
    self.tail = self.head  # Update tail to the current head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev  # Update head to the last processed node
  
singly_linked_list = SinglyLinkedList()

# Example usage:
singly_linked_list.append(10)
singly_linked_list.append(20)
singly_linked_list.append(30)
singly_linked_list.insert(1, 15)  # Insert 15 at index 1
print(singly_linked_list)  # Output: 10 -> 15 -> 20 -> 30
singly_linked_list.remove(20)  # Remove the first occurrence of 20
print(singly_linked_list)  # Output: 10 -> 15 -> 30
print(singly_linked_list.pop())  # Remove and return the last element (30)
print(singly_linked_list)  # Output: 10 -> 15
singly_linked_list[0] = 100  # Set the first element to 100
print(singly_linked_list)  # Output: 100 -> 15
print(singly_linked_list[1])  # Get the second element (15)
singly_linked_list.clear()  # Clear the list
print(singly_linked_list)  # Output: Empty List
# Reverse the list
singly_linked_list.append(1)
singly_linked_list.append(2)
singly_linked_list.append(3)
singly_linked_list.reverse() # Reverse the list
print(singly_linked_list)  # Output: 3 -> 2 -> 1
print(singly_linked_list.index(2))  # Output: 1 (index of element 2)
