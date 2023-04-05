from collections import deque


def bfs(c_x,c_y):
    while queue:
        x,y=queue.popleft()
        if board[c_x][c_y]=="S":
            return visited[c_x][c_y]
        for dx,dy in d:
            nx,ny = dx+x,dy+y
            if 0<=nx<R and 0<=ny<C:
                if board[x][y]=="S" and (board[nx][ny]=="." or board[nx][ny]=="D"):
                    board[nx][ny]="S"
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
                elif board[x][y]=="*" and (board[nx][ny]=="." or board[nx][ny]=="S"):
                    board[nx][ny]="*"
                    queue.append((nx,ny))

    return "KAKTUS"
R,C=map(int,input().split())
board= [list(input()) for _ in range(R)]
queue = deque([])
visited=[[0 for _ in range(C)] for _ in range(R)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
e_x,e_y=0,0
for i in range(R):
    for j in range(C):
        if board[i][j]=="S":
            queue.append((i,j))
        elif board[i][j]=="D":
            e_x,e_y=i,j

for i in range(R):
    for j in range(C):
        if board[i][j]=="*":
            queue.append((i,j))

print(bfs(e_x,e_y))