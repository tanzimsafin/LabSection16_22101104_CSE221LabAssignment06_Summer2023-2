import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        (cost, current) = heapq.heappop(heap)
        
        if cost > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            total_distance = cost + weight
            
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                heapq.heappush(heap, (total_distance, neighbor))
                
    return distances

with open("input2.txt", "r") as input_file:
    n, m = map(int, input_file.readline().split())
    graph = {i: {} for i in range(1, n+1)}  # Build the graph
    
    for _ in range(m):
        u, v, w = map(int, input_file.readline().split())
        graph[u][v] = w
        
    s, t = map(int, input_file.readline().split())  # Get the starting nodes
    dist_from_s = dijkstra(graph, s)  # Run Dijkstra's algorithm from both starting nodes
    dist_from_t = dijkstra(graph, t)
    
    minimum_dist = float('inf')
    meeting_node = -1
    
    for node in range(1, n+1):
        if node in dist_from_s and node in dist_from_t:
            total_dist = max(dist_from_s[node], dist_from_t[node])
            
            if total_dist < minimum_dist:
                minimum_dist = total_dist
                meeting_node = node

with open("output2.txt", "w") as output_file:
    if meeting_node == -1:
        output_file.write("Impossible")
    else:
        output_file.write(f" Time : {minimum_dist} \n Node : {meeting_node}")
