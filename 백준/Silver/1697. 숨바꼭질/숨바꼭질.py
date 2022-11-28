import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_num = 100001
visited = [0 for _ in range(max_num)]


def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        for i in [x-1, x+1, 2*x]:
            if 0 <= i < max_num and visited[i] == 0:
                visited[i] = visited[x]+1
                queue.append(i)


bfs(n)

