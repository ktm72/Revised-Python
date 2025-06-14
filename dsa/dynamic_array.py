import ctypes

class DynamicArray:
  def __init__(self):
    self.n = 0  # Count of elements
    self.capacity = 1  # Initial capacity
    self.array = self._make_array(self.capacity)

  def __len__(self):
    return self.n

# Direct index access
  def __getitem__(self, index):
    if 0 <= index < self.n:
      return self.array[index]
    raise IndexError('Index out of bounds')
  
# Direct index assignment
  def __setitem__(self, index, value):
    if 0 <= index < self.n:
      self.array[index] = value
    else:
      raise IndexError('Index out of bounds')

#  Add an element at the end
  def append(self, item):
    if self.n == self.capacity:
      self._resize(2 * self.capacity)
    self.array[self.n] = item
    self.n += 1

# Insert element at a given index
  def insert(self, index, item):
    if self.n == self.capacity:
      self._resize(2 * self.capacity)
    for i in range(self.n, index, -1):
      self.array[i] = self.array[i - 1]
    self.array[index] = item
    self.n += 1

# Remove first occurrence
  def remove(self, item):
    for i in range(self.n):
      if self.array[i] == item:
        for j in range(i, self.n - 1):
          self.array[j] = self.array[j + 1]
        # Clear the last element
        self.array[self.n - 1] = None
        self.n -= 1
        return
    raise ValueError("Item not found")

# Remove and return the last element
  def pop(self):
    if self.n == 0:
      raise IndexError("Pop from empty array")
    item = self.array[self.n - 1]
    self.array[self.n - 1] = None
    self.n -= 1
    return item

  def _resize(self, new_cap):
    new_array = self._make_array(new_cap)
    for i in range(self.n):
      new_array[i] = self.array[i]
    self.array = new_array
    self.capacity = new_cap

  def _make_array(self, cap):
    return (cap * ctypes.py_object)()

  def __str__(self):
    return "[" + ", ".join(str(self.array[i]) for i in range(self.n)) + "]"

arr = DynamicArray()
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)  # [10, 20, 30]

arr.insert(1, 15)
print(arr)  # [10, 15, 20, 30]

arr.remove(20)
print(arr)  # [10, 15, 30]

print(arr.pop())  # 30
print(arr)        # [10, 15]

print(arr[1])     # 15
arr[1] = 100
print(arr)        # [10, 100]
print(arr)  # 2

# | Operation             | Time Complexity                     | Space Complexity | Notes                        |
# | --------------------- | ----------------------------------- | ---------------- | ---------------------------- |
# | `append(item)`        | **Amortized O(1)**, Worst-case O(n) | O(1)             | Doubles capacity when full   |
# | `insert(index, item)` | O(n)                                | O(1)             | Shifts elements to the right |
# | `remove(item)`        | O(n)                                | O(1)             | Searches and shifts left     |
# | `pop()`               | O(1)                                | O(1)             | Removes last element         |
# | `__getitem__(i)`      | O(1)                                | O(1)             | Direct index access          |
# | `__setitem__(i, v)`   | O(1)                                | O(1)             | Direct index assignment      |
# | `__len__()`           | O(1)                                | O(1)             | Just returns the count       |
# | `_resize()`           | O(n)                                | O(n)             | Copies elements to new array |
# | `__str__()`           | O(n)                                | O(n)             | Joins elements into a string |
