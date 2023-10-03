result = 0
def dfs(sum, idx):
    global result, visited
    if idx >= N:
        return
    sum+=lst[idx]
    if sum==S:
        result+=1
        
    
    dfs(sum-lst[idx], idx+1)
    dfs(sum, idx+1)
    
    

N, S = map(int,input().split())
visited = [False for _ in range(N)]
lst = list(map(int,input().split()))
dfs(0, 0)
print(result)