import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
visited = [float("INF") for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w, v))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    while q:
        cost, new_start = heapq.heappop(q)
        if visited[new_start] < cost:
            continue
        for c, s in graph[new_start]:
            new_cost = c+cost
            if visited[s] > new_cost:
                heapq.heappush(q, (new_cost, s))
                visited[s] = new_cost

dijkstra(K)

for i in range(1, V+1):
    if visited[i]>(V*E)+1:
        print("INF")
        continue
    print(visited[i])