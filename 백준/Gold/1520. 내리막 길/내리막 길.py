def dfs(x,y):
    global dp
    if x==M-1 and y==N-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        nx,ny = dx[i]+x, dy[i]+y
        if 0<=nx<M and 0<=ny<N and maps[nx][ny]<maps[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]




M,N=map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(dfs(0,0))