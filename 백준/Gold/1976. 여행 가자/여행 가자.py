def find(a):
    if parent[a]==a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N)]
for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(len(lst)):
        if lst[j]==0:
            continue
        union(i,j)

map_lst = list(map(int,input().split()))
result = set([find(i-1) for i in map_lst])

if len(result)==1:
    print("YES")
else:
    print("NO")