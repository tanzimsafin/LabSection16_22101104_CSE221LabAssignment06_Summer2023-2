import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        (cost, current) = heapq.heappop(heap)
        if cost > dist[current]:
            continue
        for neighbor, weight in graph[current].items():
            total_dist = cost + weight
            if total_dist < dist[neighbor]:
                dist[neighbor] = total_dist
                heapq.heappush(heap, (total_dist, neighbor))
    return dist


with open("input2.txt","r") as f1 :
    n, m = map(int, f1.readline().split())
    graph = {i: {} for i in range(1, n+1)}        # Build the graph
    for i in range(m):
      u, v, w = map(int, f1.readline().split())
      graph[u][v] = w


    s, t = map(int, f1.readline().split())               # Get the starting nodes
    dist_from_s = dijkstra(graph, s)                # Run Dijkstra's algorithm from both starting nodes
    dist_from_t = dijkstra(graph, t)


    minimum_dist = float('inf')
    meeting_point = -1
    for node in range(1, n+1):
      if node in dist_from_s and node in dist_from_t:
         total_dist = max(dist_from_s[node] , dist_from_t[node])
         if total_dist < minimum_dist:
            minimum_dist = total_dist
            meeting_point = node


with open("output2.txt","w") as f2 :
    if meeting_point == -1:
      f2.write("Impossible")
    else:
      f2.write(f" Time : {minimum_dist} \n Node : {meeting_point}")