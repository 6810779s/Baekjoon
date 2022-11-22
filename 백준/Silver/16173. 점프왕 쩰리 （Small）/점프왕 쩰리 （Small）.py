import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(i, j):
    if i >= n or j >= n or visited[i][j] == True:
        return
    visited[i][j] = True
    dx = arr[i][j]
    dfs(i, j+dx)
    dfs(i+dx, j)


dfs(0, 0)
if visited[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")