from collections import deque

def bfs(s_x,s_y, t_x,t_y):
    global visited,result
    queue = deque([(s_x,s_y)])
    visited[s_x][s_y] = 1

    while queue:
        x, y = queue.popleft()
        if x == t_x and y == t_y:
            result = min(result,visited[x][y]-1)
            
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
                
        
T = int(input())
for _ in range(T):
    N = int(input())
    result = N*N+1
    s_x, s_y = map(int,input().split())
    t_x, t_y = map(int, input().split())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    bfs(s_x,s_y, t_x,t_y)
    print(result)