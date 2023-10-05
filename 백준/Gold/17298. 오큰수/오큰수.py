n=int(input())
num_lst=list(map(int,input().split()))
res=[-1 for _ in range(n)]
stack=[]
for i in range(n):
    while stack and num_lst[stack[-1]]<num_lst[i]:
        res[stack.pop()]=num_lst[i]
    stack.append(i)
    
print(*res)