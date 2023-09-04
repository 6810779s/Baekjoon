from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(s_r,s_c):
    global visited
    q = deque([(s_r, s_c)])
    visited[s_r][s_c] = True
    while q:
        row, col = q.popleft()
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if (row, col) in bridge[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True

    

N, K, R = map(int,input().split())
visited = [[False for _ in range(N)] for _ in range(N)]
bridge = [[[] for _ in range(N)] for _ in range(N)]
cow_info = []

for _ in range(R):
    r1,c1,r2,c2 = map(int,input().split())
    bridge[r1 - 1][c1 - 1].append((r2 - 1,c2 - 1))
    bridge[r2 - 1][c2 - 1].append((r1 - 1,c1 - 1))
    

for _ in range(K):
    r,c = map(int,input().split())
    cow_info.append((r-1, c-1))


result = 0
for i in range(K):
    visited = [[False for _ in range(N)] for _ in range(N)] 
    bfs(cow_info[i][0], cow_info[i][1])
    for j in range(i+1,K):
        if not visited[cow_info[j][0]][cow_info[j][1]]:
            result+=1
        

print(result)
