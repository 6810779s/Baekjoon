import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


def result():
    visited = [0 for _ in range(n+1)]
    for i in range(m):
        person, enemy = map(int, input().split())
        graph[person].append(enemy)
        graph[enemy].append(person)

    def bfs(v):
        queue = deque([v])

        while queue:
            p = queue.popleft()
            for i in graph[p]:
                if visited[i] == 0:
                    visited[i] = visited[p]*(-1)
                    queue.append(i)
                elif visited[i] == visited[p]:
                    print(0)
                    exit(0)

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i)
    print(1)


result()
