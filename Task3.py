with open('input3.txt','r')as f:
    import math
    s=f.readline().split( )
    vertex=int(s[0])
    edge=int(s[1])
    graph = {i:[] for i in range(1, vertex + 1)}
    for i in range(1,edge+1):
      a=f.readline().strip().split(' ')
      m=int(a[0])
      n=int(a[1])
      w=int(a[2])
      if m in graph:
        graph[m].append((n,w))
def djkstra(source,end):
  import math
  distance=[math.inf]*(vertex+1)
  my_set=set() 
  distance[source]=0 
  my_set.add((0,source))
  while my_set:
   top=my_set.pop()
   for i,j in graph[top[1]]:
    new_dist = max(top[0],j)
    if distance[i]>new_dist: 
     distance[i]=new_dist
     my_set.add((new_dist,i))
  return distance[end]
with open('output3.txt','w') as m:
  min_danger = djkstra(1,vertex)
  m.write(str(min_danger))
  