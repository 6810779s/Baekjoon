import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [float("INF") for _ in range(n+1)]

for _ in range(m):
    s_city, e_city, cost = map(int, input().split())
    graph[s_city].append((cost, e_city))

start_city, end_city = map(int, input().split())

def dijkstra(x):
    hq = []
    heapq.heappush(hq, (0, x))
    visited[x] = 0
    while hq:
        cost, end = heapq.heappop(hq)
        if visited[end] < cost:
            continue
        for n_cost, n_end in graph[end]:
            cost_total = cost + n_cost
            if visited[n_end] > cost_total:
                visited[n_end] = cost_total
                heapq.heappush(hq, (cost_total, n_end))

dijkstra(start_city)
print(visited[end_city])