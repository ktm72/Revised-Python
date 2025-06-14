class Node:
  def __init__(self):
    self.data = None
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, data):
    new_node = Node()
    new_node.data = data
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.size += 1

  def insert(self, data, index):
    new_node = Node()
    new_node.data = data
    if index < 0 or index > self.size:
      raise IndexError("Index out of bounds")
    self.size += 1
    if index == 0:
      new_node.next = self.head
      if self.head:
        self.head.prev = new_node
      self.head = new_node
      if not self.tail:
        self.tail = new_node
    else:
      current = self.head
      for _ in range(index - 1):
        if current is None:
          raise IndexError("Index out of bounds")
        current = current.next
      new_node.next = current.next
      new_node.prev = current
      if current.next:
        current.next.prev = new_node
      current.next = new_node
      if new_node.next is None:
        self.tail = new_node

  def remove(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current.prev:
          current.prev.next = current.next
        else:
          self.head = current.next
        if current.next:
          current.next.prev = current.prev
        else:                                                                                                                                             
          self.tail = current.prev
        self.size -= 1
        return
      current = current.next
    raise ValueError("Data not found in the list")
  
  def pop(self, index=None):
    if index is not None and (index < 0 or index >= self.size):
      raise IndexError("Index out of bounds")
    if index is None and self.size == 0:
      raise IndexError("Pop from empty list")
    self.size -= 1
    if index is None:
      if not self.tail:
        raise IndexError("Pop from empty list")
      data = self.tail.data
      if self.tail.prev:
        self.tail = self.tail.prev
        self.tail.next = None
      else:
        self.head = None
        self.tail = None
      return data
    else:
      current = self.head
      for _ in range(index):
        if current is None:
          raise IndexError("Index out of bounds")
        current = current.next
      if current.prev:
        current.prev.next = current.next
      else:
        self.head = current.next
      if current.next:
        current.next.prev = current.prev
      else:
        self.tail = current.prev
      return current.data
    
  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0
  def reverse(self):
    current = self.head
    prev = None
    self.tail = current
    while current:
      next_node = current.next
      current.next = prev
      current.prev = next_node
      prev = current
      current = next_node
    self.head = prev
  def find(self, data):
    current = self.head
    while current:
      if current.data == data:
        return current
      current = current.next
    return None
  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  def __repr__(self):
    if not self.head:
      return "(empty list)"
    return " <-> ".join(str(data) for data in self)
  def __len__(self):
    return self.size
  def __getitem__(self, index):
    if index < 0:
      index += len(self)
    if index < 0 or index >= len(self):
      raise IndexError("Index out of bounds")
    current = self.head
    for _ in range(index):
      current = current.next
    return current.data if current else None
  def __setitem__(self, index, value):
    if index < 0:
      index += len(self)
    if index < 0 or index >= len(self):
      raise IndexError("Index out of bounds")
    current = self.head
    for _ in range(index):
      current = current.next
    if current:
      current.data = value
    else:
      raise IndexError("Index out of bounds")
  def __contains__(self, data):
    current = self.head
    while current:
      if current.data == data:
        return True
      current = current.next
    return False
  def index(self, data):
    current = self.head
    index = 0
    while current:
      if current.data == data:
        return index
      current = current.next
      index += 1
    raise ValueError("Data not found in the list")
  def extend(self, other):
    if not isinstance(other, DoublyLinkedList):
      raise TypeError("Can only extend with another DoublyLinkedList")
    if not other.head:
      return
    if not self.head:
      self.head = other.head
      self.tail = other.tail
    else:
      self.tail.next = other.head
      other.head.prev = self.tail
      self.tail = other.tail
    self.size += other.size

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll)  # Output: 1 <-> 2 <-> 3
dll.insert(4, 1)
print(dll)  # Output: 1 <-> 4 <-> 2 <-> 3
dll.insert(5, 0)
print(dll)  # Output: 5 <-> 1 <-> 4 <-> 2 <-> 3
dll.remove(2)
print(dll)  # Output: 5 <-> 1 <-> 4 <-> 3
print(dll.pop())  # Output: 3
print(dll)  # Output: 5 <-> 1 <-> 4
dll.reverse()
print(dll)  # Output: 4 <-> 1 <-> 5
print(dll.find(1))  # Find node with data 1
print(dll[0])  # Accessing first element
print(len(dll))  # Length of the list
print(3 in dll)  # Check if 3 is in the list
print(dll.index(4))  # Get index of element 4
dll[1] = 10  # Set second element to 10
print(dll)  # Output: 4 <-> 10 <-> 5

dll2 = DoublyLinkedList()
dll2.append(6)
dll2.append(7)
dll.extend(dll2)
print(dll)  # Output: 4 <-> 10 <-> 5 <-> 6 <-> 7
print(len(dll))  # Length of the list after extending
print(len(dll2))  # Length of the second list
dll2.clear()  # Clear the second list
print(dll2)  # Output: (empty list)