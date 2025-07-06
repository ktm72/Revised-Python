class MinHeap:
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
        """Remove and return the smallest element from the heap."""
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
        # While the current node is not the root and is smaller than its parent
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # print(
            #     f"current index: {index}, parent index: {self.parent(index)}")
            # print(
            #     f"Swapping current item {self.heap[index]} with parent {self.heap[self.parent(index)]}")
            # Swap the current node with its parent
            self.heap[index], self.heap[self.parent(
                index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def heapify_down(self, index):
        """Restore the heap property by moving the element at index down."""
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find the smallest among the current node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def peek(self):
        """Return the smallest element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def __repr__(self):
        """Return a string representation of the heap."""
        return str(self.heap)


# Example usage:
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(5)
    min_heap.insert(15)
    min_heap.insert(1)
    min_heap.insert(7)

    print("Heap after inserts:", min_heap)
    print("Extracted min:", min_heap.remove())
    print("Heap after extracting min:", min_heap)
    print("Peek at min:", min_heap.peek())
    print("Extracted min:", min_heap.remove())
    print("Heap after extracting another min:", min_heap)
