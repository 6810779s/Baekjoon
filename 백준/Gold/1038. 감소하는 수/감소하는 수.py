def dfs(lst,limit, depth):
    global cnt
    if limit == depth:
        if cnt==N:
            print(''.join(lst))
            exit()
        cnt+=1
        return
    for j in range(10):
        if lst and int(lst[-1])>j:
            dfs(lst+[str(j)], limit, depth+1)
        elif not lst:
            dfs(lst+[str(j)],limit, depth+1)
    

    
N = int(input())
# 0 ~ 9로 조합
cnt = 0

for i in range(1,11): # 감소하는 수 중 제일 큰 수 9876543210, 1자릿수부터 10자릿수까지만 가능
    dfs([], i, 0)
print(-1)