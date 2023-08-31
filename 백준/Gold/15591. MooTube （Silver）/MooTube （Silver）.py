from collections import deque
N,Q =map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))



for i in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    visited[v] = True
    result = 0
    q = deque([(v, 1000000001)])
    while q:
        v, usado = q.popleft()
        for n_v, n_usado in graph[v]:
            n_usado = min(usado, n_usado)
            if n_usado >= k and not visited[n_v]:
                result+=1
                q.append((n_v,n_usado))
                visited[n_v]=True
    print(result)






