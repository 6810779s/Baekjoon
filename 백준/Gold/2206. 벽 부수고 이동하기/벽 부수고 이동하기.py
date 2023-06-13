
from collections import deque

def bfs(x, y, z):
    queue = deque([(x, y, z)])
    visited[x][y][z] = 1
    while queue:
        a,b,c = queue.popleft()
        if a==N-1 and b==M-1:
            return visited[a][b][c]
        for i in range(4):
            nx,ny = a+dx[i], b+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == '1' and c==0:
                    visited[nx][ny][1] = visited[a][b][0]+1
                    queue.append((nx,ny,1))
                elif board[nx][ny] == '0' and not visited[nx][ny][c]:
                    visited[nx][ny][c] = visited[a][b][c]+1
                    queue.append((nx,ny,c))
    return -1

N,M=map(int,input().split())
board = [list(input()) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
print(bfs(0,0,0))