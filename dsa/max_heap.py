class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        """Return the index of the parent node."""
        return (index - 1) // 2

    def left_child(self, index):
        """Return the index of the left child node."""
        return 2 * index + 1

    def right_child(self, index):
        """Return the index of the right child node."""
        return 2 * index + 2

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)  # Add the key at the end
        self.heapify_up(len(self.heap) - 1)  # Restore the heap property

    def remove(self):
        """Remove and return the largest element from the heap."""
        if len(self.heap) == 0:
            raise IndexError("Extract from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root with the last element and remove the root
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)  # Restore the heap property
        return root

    def heapify_up(self, index):
        """Restore the heap property by moving the element at index up."""
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            # Swap the current node with its parent
            self.heap[index], self.heap[self.parent(
                index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def heapify_down(self, index):
        """Restore the heap property by moving the element at index down."""
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find the largest among the current node and its children
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and continue heapifying
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def peek(self):
        """Return the largest element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def __repr__(self):
        """Return a string representation of the heap."""
        return str(self.heap)


# Example usage:
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(15)
    max_heap.insert(1)
    max_heap.insert(7)

    print("Heap after inserts:", max_heap)
    print("Extracted max:", max_heap.remove())
    print("Heap after extracting max:", max_heap)
    print("Peek at max:", max_heap.peek())
    print("Extracted max:", max_heap.remove())
    print("Heap after extracting another max:", max_heap)
