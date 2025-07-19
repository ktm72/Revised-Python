import heapq

# def huffman_coding(frequencies):
#   pq = []
#   for char, freq in frequencies.items():
#     heapq.heappush(pq, (freq, char))

#   while len(pq) > 1:
#     freq1, char1 = heapq.heappop(pq)
#     freq2, char2 = heapq.heappop(pq)
#     heapq.heappush(pq, (freq1 + freq2, char1 + char2))

#   return heapq.heappop(pq)


# Example usage:
# if __name__ == "__main__":
#   frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
#   print("Huffman Tree:", huffman_coding(frequencies))

# Huffman Coding Implementation
class HuffmanNode:
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq


def build_huffman_tree(frequencies):
  """Build the Huffman Tree and return its root."""
  pq = []
  for char, freq in frequencies.items():
    heapq.heappush(pq, HuffmanNode(char, freq))

  while len(pq) > 1:
    # Remove the two nodes with the smallest frequencies
    left = heapq.heappop(pq)
    right = heapq.heappop(pq)

    # Create a new internal node with the combined frequency
    merged = HuffmanNode(None, left.freq + right.freq)
    merged.left = left
    merged.right = right

    heapq.heappush(pq, merged)

  # Return the root of the Huffman Tree
  return heapq.heappop(pq)


def generate_huffman_codes(root, current_code="", codes={}):
  """Generate Huffman codes by traversing the Huffman Tree."""
  # print("Current node:", f"{root.char} with frequency: {root.freq}" if root else "No char")
  if root is None:
    return

  # If it's a leaf node, add the character and its code to the dictionary
  if root.char is not None:
    # print("Leaf node found:", root.char, "with code:", current_code) 
    codes[root.char] = current_code

  generate_huffman_codes(root.left, current_code + "0", codes)
  generate_huffman_codes(root.right, current_code + "1", codes)

  return codes


def encode(data, codes):
  """Encode the input data using the Huffman codes."""
  encoded_data = ""
  for char in data:
    encoded_data += codes[char]
  return encoded_data


def decode(encoded_data, root):
  """Decode the encoded data using the Huffman Tree."""
  decoded_data = ""
  current_node = root

  for bit in encoded_data:
    # print("Current bit:", bit)
    if bit == "0":
      current_node = current_node.left
    else:
      current_node = current_node.right
    # print("Current node char:", current_node.char)
    # If it's a leaf node, append the character to the result
    if current_node.char is not None:
      # print("Decoded character:", current_node.char)
      decoded_data += current_node.char
      # print("Current decoded data:", decoded_data)
      # Reset to the root for the next character
      current_node = root  

  return decoded_data


# Example usage:
if __name__ == "__main__":
  # Input data and frequencies
  frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
  data = "ABCDEDACBF"

  # Build the Huffman Tree
  root = build_huffman_tree(frequencies)
  print("Huffman Tree Root Frequency:", root.freq)

  # Generate Huffman codes
  codes = generate_huffman_codes(root)
  print("Huffman Codes:", codes)

  # Encode the data
  encoded_data = encode(data, codes)
  print("Encoded Data:", encoded_data)

  # Decode the data
  decoded_data = decode(encoded_data, root)
  print("Decoded Data:", decoded_data)