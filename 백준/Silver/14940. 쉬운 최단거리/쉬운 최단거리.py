from collections import deque

n,m = map(int,input().split())

x, y = 0, 0
board = []

for i in range(n):
    lst = list(map(int,input().split()))
    board.append(lst)
    for j in range(m):
        if lst[j] == 2:
            x, y = i, j
            break

result=[[-1 for _ in range(m)] for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(s_x, s_y):
    q = deque([(s_x, s_y)])
    visited[s_x][s_y] = True
    result[s_x][s_y] = 0
    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx+dx[i], sy+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny]==0:
                    result[nx][ny] = 0
                elif board[nx][ny]==1:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    result[nx][ny] = result[sx][sy] + 1

bfs(x,y)
for i in range(n):
    for j in range(m):
        if board[i][j]==0 and result[i][j]==-1:
            print(0, end = ' ')
        else:
            print(result[i][j], end=' ')
    print()