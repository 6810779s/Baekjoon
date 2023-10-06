N = int(input())
A = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = -101
def dfs(lst, depth, sum):
    global result
    if len(lst) == N:
        result = max(result, sum)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if not lst:
                dfs(lst+[A[i]], i+1, 0)
            else:
                dfs(lst+[A[i]], i+1, sum+abs(lst[-1]-A[i]))
            visited[i] = False

dfs([], 0, 0)
print(result)