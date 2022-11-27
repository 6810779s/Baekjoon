import sys
input = sys.stdin.readline

n = int(input())
v = [[False for _ in range(n)] for _ in range(n)]
arr = [str(input()) for _ in range(n)]
dn = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cnt = 0
res = []


def dfs(i, j):
    global cnt
    v[i][j] = True
    if arr[i][j] == "1":
        cnt += 1
    for x, y in dn:
        dx = i+x
        dy = j+y
        if 0 <= dx < n and 0 <= dy < n:
            if v[dx][dy] == False and arr[i][j] == "1":
                dfs(dx, dy)


for i in range(n):
    for j in range(n):
        if v[i][j] == False and arr[i][j] == "1":
            dfs(i, j)
            res.append(cnt)
            cnt = 0
res.sort()
print(len(res))
for i in res:
    print(i)
