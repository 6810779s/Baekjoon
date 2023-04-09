def dfs(cnt,lst):
    global visited,num_lst,result
    if cnt==M:
        print(*lst)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            lst.append(num_lst[i])
            dfs(cnt+1,lst)
            lst.pop()
            visited[i]=False


result = []
N, M=map(int,input().split())
visited = [False for _ in range(N)]
num_lst = list(map(int,input().split()))
num_lst.sort()
dfs(0,[])