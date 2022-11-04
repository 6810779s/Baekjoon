import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]


def bfs(v):
    cnt = 0
    visited = [False]*(n+1)
    visited[v] = True
    queue = deque([v])
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
