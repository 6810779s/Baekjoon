from collections import deque

def bfs(cur_x,cur_y):
    visited=[[False for _ in range(m)] for _ in range(n)]
    queue=deque([(cur_x,cur_y)])
    visited[cur_x][cur_y]=True
    melt=[]
    while queue:
        x,y=queue.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if cheese[nx][ny]==0:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                else:
                    if (nx,ny) not in melt:
                        melt.append((nx,ny))
    return melt

def check(lst):
    total =0 
    for row in lst:
        total+=sum(row)
    return total

n,m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
total = []
cnt = 0
total_cheese = check(cheese)
total.append(total_cheese)
while True:
    melt_lst = bfs(0,0)
    if not melt_lst:
        break
    total_cheese-=len(melt_lst)
    total.append(total_cheese)
    for i,j in melt_lst:
        cheese[i][j]=0
    cnt+=1
print(cnt)
print(total[-2])


