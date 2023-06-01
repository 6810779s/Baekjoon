def count_odd(n):
    cnt=0
    for s in n:
        if int(s)%2:
            cnt+=1
    return cnt

def dfs(n,cnt):
    global minNum,maxNum
    s_n = str(n)
    cnt+=count_odd(s_n)
    if len(s_n)==1:
        minNum=min(minNum,cnt)
        maxNum=max(maxNum,cnt)
        return
    elif len(s_n)==2:
        dfs(int(s_n[0])+int(s_n[1]),cnt)
    elif len(s_n)>=3:
        for i in range(1,len(s_n)-1):
            for j in range(i+1,len(s_n)):
                newNum = int(s_n[:i])+int(s_n[i:j])+int(s_n[j:])
                dfs(newNum,cnt)

N = int(input())
minNum=float('inf')
maxNum=0
dfs(N,0)
print(minNum, maxNum)