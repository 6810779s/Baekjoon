from collections import deque

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    
    def bfs(start, end, cost):
        q = deque()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visited=[[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if maps[i][j] == start:
                    q.append((i,j, 0))
                    visited[i][j] = True
        
        while q:
            x, y, cost = q.popleft()
            if maps[x][y] == end:
                return cost
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx,ny, cost+1))
                        
        return -1
    
    path1 = bfs('S', 'L', 0)
    path2 = bfs('L', 'E', 0)
    if path1!=-1 and path2!=-1:
        answer = path1 + path2
        
    return answer if answer else -1