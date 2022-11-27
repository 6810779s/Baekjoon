import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [str(input()) for _ in range(n)]
v = [[False for _ in range(n)] for _ in range(n)]
dn = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    cnt = 0
    queue = deque([(i, j)])
    v[i][j] = True
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for q, w in dn:
            dx = x+q
            dy = y+w
            if 0 <= dx < n and 0 <= dy < n:
                if v[dx][dy] == False and arr[dx][dy] == "1":
                    queue.append((dx, dy))
                    v[dx][dy] = True

    return cnt


res = []
for i in range(n):
    for j in range(n):
        if v[i][j] == False and arr[i][j] == "1":
            res.append(bfs(i, j))

print(len(res))
res.sort()
for i in res:
    print(i)
