import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro_arr = []

for _ in range(n):
    string = str(input())
    arr = []
    for i in range(m):
        arr.append(int(string[i]))
    miro_arr.append(arr)


def bfs(a, b):
    global miro_arr
    visited = [[0]*m for _ in range(n)]
    dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    queue = deque([(a, b)])
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y]
        for i, j in dir:
            nx = i+x
            ny = j+y
            if 0 <= nx < n and 0 <= ny < m:
                if miro_arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y]+1
print(bfs(0, 0))