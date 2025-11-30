import heapq

def dijkstra(graph, start):
    # graph: dict {node: list of (neighbor, weight)}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

# Example graph as adjacency list
graph = {
       '0': [('1', 4), ('2', 8)],
       '1': [('4', 6)],
       '2': [('3', 2)],
       '3': [('4', 10)],
       '4': []
   }
start_node = '0'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")