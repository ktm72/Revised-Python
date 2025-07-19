import heapq

def dijkstra(graph, start):
  pq = []  # Priority queue
  heapq.heappush(pq, (0, start))  # (distance, node)
  distances = {node: float('inf') for node in graph}
  # print("Initial distances:", distances)
  distances[start] = 0

  while pq:
    current_distance, current_node = heapq.heappop(pq)

    # Skip if the current distance is not optimal
    if current_distance > distances[current_node]:
      continue
    # print(f"Visiting node {current_node} with distance {current_distance}")
    for neighbor, weight in graph[current_node]:
      # print(f"Checking neighbor {neighbor} with weight {weight}")
      distance = current_distance + weight

      # If a shorter path is found
      if distance < distances[neighbor]:
        # print(f"Updating distance for {neighbor} to {distance}")
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))

  return distances


# Example usage:
if __name__ == "__main__":
  graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
  }

  start_node = 'A'
  print("Shortest distances from node A:", dijkstra(graph, start_node))