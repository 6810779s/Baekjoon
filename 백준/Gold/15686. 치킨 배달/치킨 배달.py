from itertools import combinations

N,M = map(int, input().split())
board = []
home=[]
chicken=[]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j]==1:
            home.append((i,j))
        elif lst[j]==2:
            chicken.append((i,j))
    board.append(lst)

t = combinations(chicken, M)
def cal(com):
    s_res = 0
    for hx,hy in home:
        min_d = N*N+1
        for dx in com:
            x,y = dx
            min_d = min(min_d, abs(hx-x)+abs(hy-y))
        s_res+=min_d
    return s_res

total = float("INF")
for i in t:
    total=min(total,cal(i))

print(total)
