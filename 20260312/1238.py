import sys
from collections import defaultdict
import heapq

n,m,x = map(int, sys.stdin.readline().split())
road = defaultdict(list)
result = []

for _ in range(m):
    s,e,t = map(int,sys.stdin.readline().split())
    road[s].append((e,t))

def dijkstra(start, graph):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [] 
    heapq.heappush(pq, (0,start))

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist>dist[cur_node]:
            continue

        for e,t in road[cur_node]:
            distance = cur_dist + t

            if distance < dist[e]:
                dist[e] = distance
                heapq.heappush(pq, (distance, e))
    return dist

dist_from_x = dijkstra(x,road)

for i in range(1,n+1):
    dist_to_x = dijkstra(i,road)[x]
    result.append(dist_from_x[i]+dist_to_x)

print(max(result))


