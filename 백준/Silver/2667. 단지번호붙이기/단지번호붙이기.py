from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    cnt = 1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and map_lst[nx][ny]=="1" and not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt



n = int(input())
map_lst = [list(input()) for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
home_cnt=0
res_cnt = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and map_lst[i][j]=="1":
            res_cnt.append(bfs(i,j))
            home_cnt+=1

res_cnt.sort()
print(home_cnt)
for i in range(home_cnt):
    print(res_cnt[i])