from collections import deque
def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt


n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
total_cnt=0
max_cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j]:
            total_cnt+=1
            max_cnt=max(max_cnt,bfs(i,j))

print(total_cnt)
print(max_cnt)