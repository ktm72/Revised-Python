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

  def __repr__(self):
    return str(self.items)


def hanoi_tower(n, source, target, auxiliary):
  """Solve Tower of Hanoi using stacks."""
  if n <= 0:
    return

  print(f"running for {n} disks")
  # Move n-1 disks from source to auxiliary using target as a buffer
  hanoi_tower(n - 1, source, auxiliary, target)

  # Move the nth disk from source to target
  disk = source.pop()
  print(f"target before pushing disk {target}")
  target.push(disk)
  print(f"Move disk {disk} from {source} to {target}")

  # Print the state of all stacks after each move
  print(f"State after moving disk {disk}:")
  print(f"Source: {source}")
  print(f"Target: {target}")
  print(f"Auxiliary: {auxiliary}")
  print("-" * 30)

  # Move the n-1 disks from auxiliary to target using source as a buffer
  hanoi_tower(n - 1, auxiliary, target, source)

def hanoi_tower_iterative(n, source, target, auxiliary):
  """Solve Tower of Hanoi iteratively using stacks."""
  total_moves = 2 ** n - 1  # Total number of moves required
  rods = [source, target, auxiliary]  # Rods represented as stacks

  # If the number of disks is even, swap target and auxiliary
  if n % 2 == 0:
    rods[1], rods[2] = rods[2], rods[1]

  for move in range(1, total_moves + 1):
    # Determine the source and destination rods for the current move
    if move % 3 == 1:
      from_rod, to_rod = rods[0], rods[1]
    elif move % 3 == 2:
      from_rod, to_rod = rods[0], rods[2]
    else:
      from_rod, to_rod = rods[1], rods[2]

    # Ensure valid moves (smallest disk always moves)
    if from_rod.is_empty() or (not to_rod.is_empty() and from_rod.peek() > to_rod.peek()):
      from_rod, to_rod = to_rod, from_rod

    # Perform the move
    disk = from_rod.pop()
    if disk is not None:
      to_rod.push(disk)

    # Print the state of the rods after each move
    print(f"Move disk {disk} from {from_rod} to {to_rod}")
    print(f"State after move {move}:")
    print(f"Source: {source}")
    print(f"Target: {target}")
    print(f"Auxiliary: {auxiliary}")
    print("-" * 30)


# Example usage:
if __name__ == "__main__":
  n = 3  # Number of disks

  # Create three stacks representing the rods
  source = Stack()
  target = Stack()
  auxiliary = Stack()

  # Initialize the source rod with disks (largest at the bottom)
  for i in range(n, 0, -1):
      source.push(i)

  print("Initial state:")
  print(f"Source: {source}")
  print(f"Target: {target}")
  print(f"Auxiliary: {auxiliary}")

  # Solve the Tower of Hanoi
  hanoi_tower(n, source, target, auxiliary)

  # # Solve the Tower of Hanoi iteratively
  # hanoi_tower_iterative(n, source, target, auxiliary)

  print("Final state:")
  print(f"Source: {source}")
  print(f"Target: {target}")
  print(f"Auxiliary: {auxiliary}")