class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size
  
  def append(self, item):
    node = Node(item)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.size += 1

  def insert(self, index, item):
    if index < 0 or index > self.size:
      raise IndexError(f"Index {index} out of bounds")
    new_node = Node(item)
    # if index == 0:
    #   new_node.next = self.head
    #   self.head = new_node
    #   if not self.tail:
    #     self.tail = new_node
    if index == 0 and not self.head:
      self.head = new_node
      self.tail = new_node
    elif index == 0:
      new_node.next = self.head
      self.head = new_node
    elif index == self.size:
      self.tail.next = new_node
      self.tail = new_node
    else:
      current = self.head # start from the head, index 0
      for _ in range(index - 1):
        current = current.next
      new_node.next = current.next
      current.next = new_node
    self.size += 1
    
  def remove(self, item):
    if not self.head:
      raise ValueError("Item not found")
    current = self.head
    if current.data == item:
      self.head = current.next
      if not self.head:
        self.tail = None
      self.size -= 1
      return
    # Traverse the list to find the item
    while current.next and current.next.data != item:
      current = current.next
    if current.next is None:
      raise ValueError("Item not found")
    current.next = current.next.next
    if not current.next:
      self.tail = current
    self.size -= 1

  def pop(self, index= None):
    if not self.head:
      raise IndexError("No elements to pop from an empty list")
    if index is None:
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
    if index < 0 or index >= self.size:
      raise IndexError(f"Index {index} out of bounds")
    if index == 0:
      item = self.head.data
      self.head = self.head.next
      if not self.head:
        self.tail = None
      self.size -= 1
      return item
    current = self.head
    for _ in range(index - 1):
      current = current.next
    item = current.next.data
    current.next = current.next.next
    if current.next is None:
      self.tail = current
    self.size -= 1
    return item

  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def __getitem__(self, index):
    if index < 0 or index >= self.size:
      raise IndexError(f"Index {index} out of bounds")
    curr = self.head
    for _ in range(index):
      curr = curr.next
    return curr.data  
  def __setitem__(self, index, value):
    if index < 0 or index >= self.size:
      raise IndexError(f"Index {index} out of bounds")
    curr = self.head
    for _ in range(index):
      curr = curr.next
    curr.data = value  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  def __repr__(self):
    return f"SinglyLinkedList([{', '.join(repr(item) for item in self)})])"

sll = SinglyLinkedList()

# Example usage:
try:
  sll.append(10)
  sll.append(20)
  sll.append(30)
  sll.insert(4, 15)
except IndexError as e:
  print(e)  # Output: Index out of bounds 
print(sll)  # Output: SinglyLinkedList([10, 15, 20, 30])
print(len(sll))  # Output: length of the list
sll.pop() # output: 30
sll.insert(1, 15)  # Insert 15 at index 1
sll.pop(2)  # Pop the item at index 2
sll[0] = 50  # Set the first item to 10
print(sll)
    

