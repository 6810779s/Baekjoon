from collections import deque

def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n+1)]
    visited=[False for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)

    def bfs(x):
        queue=deque([x])
        visited[x]=True
        while queue:
            q = queue.popleft()
            for i in graph[q]:
                if visited[i]==False:
                    visited[i]=True
                    queue.append(i)
        return 1
    
    for i in range(1,n+1):
        if visited[i]==False:
            answer+=bfs(i)
#     d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
#     def bfs(x, y):
#         queue = deque([(x, y)])
#         computers[x][y] = 0
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in d:
#                 nx, ny = dx+x, dy+y
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if computers[nx][ny] == 1:
#                         computers[nx][ny] = 0
#                         queue.append((nx, ny))
#         return 1

#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] == 1:
#                 answer += bfs(i, j)
    

    return answer

