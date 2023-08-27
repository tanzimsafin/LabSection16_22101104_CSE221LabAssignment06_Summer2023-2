with open('input1.txt','r')as f:
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
    b=f.readline()
    source=int(b)
def dijkstra_algo(source):
  import math
  distance=[math.inf]*(vertex+1)#here i created a distance array which initially contains infinity
  my_set=set() #use set data structure to store pairs contains distance and their node 
  distance[source]=0 
  my_set.add((0,source))
  while my_set:
   top=my_set.pop()
   for i,j in graph[top[1]]:
    if distance[i]>top[0]+j: #if current distance is lesser than previous stored distance then we redefined it as new sortest distance
     distance[i]=top[0]+j
     my_set.add((distance[i],i))
  for i in range(len(distance)):
    if distance[i]==math.inf:
      distance[i]=-1
  return distance
with open('output1.txt','w') as m:
  p=dijkstra_algo(source)[1:]
  for i in p:
    m.write(str(i)+' ')
    

  