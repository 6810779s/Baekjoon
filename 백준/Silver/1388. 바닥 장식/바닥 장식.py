import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]


def dfs(i, j):
    if arr[i][j] == "-":
        arr[i][j] = 1
        mx = j+1
        if mx < m and arr[i][mx] == "-":
            dfs(i, mx)
    if arr[i][j] == "|":
        arr[i][j] = 1
        ny = i+1
        if ny < n and arr[ny][j] == "|":
            dfs(ny, j)


cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 1:
            dfs(i, j)
            cnt += 1

print(cnt)