import heapq

def merge_k_sorted_lists(lists):
  pq = []
  for i, lst in enumerate(lists):
    print(f"Processing list {i}: {lst}")
    # Push the first element of each list into the priority queue
    if lst:
      heapq.heappush(pq, (lst[0], i, 0))  # (value, list index, element index)

  result = []
  while pq:
      value, list_index, element_index = heapq.heappop(pq)
      print(f"Popped value: {value} from list {list_index}, index {element_index}")
      result.append(value)

      # Push the next element from the same list
      if element_index + 1 < len(lists[list_index]):
          heapq.heappush(pq, (lists[list_index][element_index + 1], list_index, element_index + 1))

  return result


# Example usage:
if __name__ == "__main__":
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Merged list:", merge_k_sorted_lists(lists))