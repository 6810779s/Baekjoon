from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


def bfs(v):
    cnt = 1
    visited = [False]*(N+1)
    queue = deque([v])
    visited[v] = True
    while queue:
        p = queue.popleft()
        for num in graph[p]:
            if not visited[num]:
                visited[num] = True
                cnt += 1
                queue.append(num)

    return cnt

max_cnt = 1
res = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

for i in range(1, N+1):
    cnt = bfs(i)

    if cnt > max_cnt:
        max_cnt=cnt
        res=[]
        res.append(i)
    elif cnt==max_cnt:
        res.append(i)

print(*res)