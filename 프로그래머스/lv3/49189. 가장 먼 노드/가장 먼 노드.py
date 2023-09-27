from collections import deque


def bfs(s, visited,graph):
    q = deque([s])
    visited[s] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return visited
    
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited=[0 for _ in range(n+1)]
    for v in edge:
        x, y = v
        graph[x].append(y)
        graph[y].append(x)
    res = bfs(1, visited, graph)
    answer = 0
    for i in range(1, n + 1):
        if res[i] == max(res):
            answer+=1
    
    return answer