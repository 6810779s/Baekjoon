N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False for _ in range(N)]


def dfs(arr):
    global result
    if len(arr) == M:
        print(*arr)
        return
    pre = 0
    for i in range(N):
        if not visited[i] and pre != lst[i]:
            visited[i] = True
            pre = lst[i]
            dfs(arr+[lst[i]])
            visited[i] = False

dfs([])