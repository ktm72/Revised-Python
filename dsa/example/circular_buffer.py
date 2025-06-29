class CircularBuffer:
  def __init__(self, capacity):
    """Initialize the circular buffer with a fixed capacity."""
    self.capacity = capacity
    self.buffer = [None] * capacity  # Fixed-size list to store data
    self.front = -1  # Points to the front of the buffer
    self.rear = -1  # Points to the rear of the buffer

  def write(self, data):
    """Write data to the buffer."""
    if self.is_full():
      raise OverflowError("Buffer is full")
    if self.is_empty():
      self.front = 0  # Set front to the first position if the buffer is empty
    self.rear = (self.rear + 1) % self.capacity  # Circular increment
    self.buffer[self.rear] = data

  def read(self):
    """Read and remove data from the buffer."""
    if self.is_empty():
      raise IndexError("Read from empty buffer")
    data = self.buffer[self.front]
    self.buffer[self.front] = None  # Clear the read position
    if self.front == self.rear:  # If the buffer becomes empty
      self.front = self.rear = -1
    else:
      self.front = (self.front + 1) % self.capacity  # Circular increment
    return data

  def is_empty(self):
    """Check if the buffer is empty."""
    return self.front == -1

  def is_full(self):
    """
    Check if the buffer is full. 
    A buffer is full if the next position of rear is front.
    Everything that written was read, so front and rear are equal.
    """
    return (self.rear + 1) % self.capacity == self.front

  def __repr__(self):
    """Return a string representation of the buffer."""
    return str(self.buffer)


# Example usage:
if __name__ == "__main__":
  capacity = 5
  buffer = CircularBuffer(capacity)

  # Write data to the buffer
  buffer.write("A")
  buffer.write("B")
  buffer.write("C")
  print("Buffer after writing 3 elements:", buffer)

  # Read data from the buffer
  print("Read:", buffer.read())
  print("Buffer after reading 1 element:", buffer)

  # Write more data to the buffer
  buffer.write("D")
  buffer.write("E")
  buffer.write("F")
  print("Buffer after writing 3 more elements:", buffer)

  # Read all data from the buffer
  while not buffer.is_empty():
    print("Read:", buffer.read())
  print("Buffer after reading all elements:", buffer)
  # Attempt to read from an empty buffer
  try:
    buffer.read()
  except IndexError as e:
    print("Error:", e)