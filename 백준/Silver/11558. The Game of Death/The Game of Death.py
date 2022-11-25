import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
graph=[]
visited=[]

def bfs(start):
    queue = deque([start])
    cnt = 0
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                if i == n:
                    return cnt
                visited[i] = 1
                queue.append(i)
    return 0


for i in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for j in range( 1, n+1):
        graph[j].append(int(input()))
    print(bfs(1))