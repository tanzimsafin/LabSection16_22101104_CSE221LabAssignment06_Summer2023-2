import math

with open('input2.txt', 'r') as f:
    s = f.readline().split()
    vertex = int(s[0])
    edge = int(s[1])
    graph = {i: [] for i in range(1, vertex + 1)}
    for i in range(edge):
        a = f.readline().strip().split(' ')
        m = int(a[0])
        n = int(a[1])
        w = int(a[2])
        if m in graph:
            graph[m].append((n, w))
    b = f.readline().split()
    S = int(b[0])
    T = int(b[1])

def find_shortest_time(start):
    distance = [math.inf] * (vertex + 1)
    distance[start] = 0
    my_set = [(0, start)]
    while my_set:
        top_dist, top_node = my_set.pop(0)
        if top_dist > distance[top_node]:
            continue
        for neighbor, weight in graph[top_node]:
            if distance[neighbor] > top_dist + weight:
                distance[neighbor] = top_dist + weight
                my_set.append((distance[neighbor], neighbor))
                my_set.sort()
    return distance

time_a = find_shortest_time(S)
time_b = find_shortest_time(T)

min_time = float('inf')
meeting_node = -1

for i in range(1, vertex + 1):
    total_time = time_a[i] + time_b[i]
    if total_time <min_time:
        min_time = total_time
        meeting_node = i

if meeting_node == -1 or time_a[meeting_node] == math.inf or time_b[meeting_node] == math.inf:
    print("Impossible")
else:
    print(min_time, meeting_node)
