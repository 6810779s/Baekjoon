import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


res = []


def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        y = queue.popleft()

        for i in graph[y]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[y]+1
                if visited[i] == k+1:
                    res.append(i)


bfs(x)

if len(res) == 0:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)
