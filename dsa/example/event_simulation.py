import heapq

class EventSimulation:
  def __init__(self):
    self.events = []

  def schedule_event(self, timestamp, event):
    heapq.heappush(self.events, (timestamp, event))

  def process_events(self):
    while self.events:
      timestamp, event = heapq.heappop(self.events)
      print(f"At time {timestamp}: {event}")


# Example usage:
if __name__ == "__main__":
  simulation = EventSimulation()
  simulation.schedule_event(5, "Event 1")
  simulation.schedule_event(1, "Event 2")
  simulation.schedule_event(3, "Event 3")

  print("Processing events:")
  simulation.process_events()