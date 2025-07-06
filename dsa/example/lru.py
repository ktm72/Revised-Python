from collections import deque

class LRUCache:
  def __init__(self, capacity):
    self.cache = {}
    self.order = deque()  # Keeps track of the usage order
    self.capacity = capacity

  def get(self, key):
    """Retrieve an item from the cache."""
    if key not in self.cache:
        return -1
    # Move the accessed key to the end (most recently used)
    self.order.remove(key)
    self.order.append(key)
    return self.cache[key]

  def put(self, key, value):
    """Add an item to the cache."""
    if key in self.cache:
      # Update the value and move the key to the end
      self.order.remove(key)
    elif len(self.cache) >= self.capacity:
      # Remove the least recently used item
      lru = self.order.popleft()
      del self.cache[lru]
    # Add the new key-value pair
    self.cache[key] = value
    self.order.append(key)

# Example usage:
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  # Output: "A"
cache.put(3, "C")    # Removes key 2 (least recently used)
print(cache.get(2))  # Output: -1 (not found)