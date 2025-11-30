def distance_vector_routing(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    # Initialize routing table
    routing_table = {node: None for node in graph}
    routing_table[source] = source

    # Repeat |V|-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    routing_table[v] = u

    return distance, routing_table

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 7},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 7, 'C': 1}
}
source = 'A'
distance, routing_table = distance_vector_routing(graph, source)
print("Distance from source:", distance)
print("Routing table:", routing_table)
