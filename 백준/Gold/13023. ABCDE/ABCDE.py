def dfs(x, depth):
    global result
    visited[x] = True
    if depth == 4:
        result = True
        return
    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[x] = False


N, M =map(int, input().split())
graph = [[] for _ in range(N)]
parent = list(range(N))
visited=[False for _ in range(N)]
result = False
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


    
for i in range(N):
    dfs(i,0)
    if result:
        break

if result:
    print(1)
else:
    print(0)