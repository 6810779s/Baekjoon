import sys
inf = 1e9
input = sys.stdin.readline

N = int(input())

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
min_cost = inf


def checkDir(x, y):
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if visited[nx][ny]:
            return False
    return True


def calCost(x, y):
    global total
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        total += arr[nx][ny]
        visited[nx][ny] = True


res = inf
total = 0


def dfs(cnt):
    global res, total
    if cnt == 3:
        res = min(res, total)
        return res

    for i in range(1, N-1):
        for j in range(1, N-1):
            if checkDir(i, j):
                calCost(i, j)
                dfs(cnt+1)
                for k in range(len(dx)):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    visited[nx][ny] = False
                    total -= arr[nx][ny]


dfs(0)
print(res)
