import sys
input=sys.stdin.readline
n,k=map(int,input().split())

answer=0
words = [set(input().strip()) for _ in range(n)]

alpha=[0]*26
for i in ("a","n","t","i","c"):
    alpha[ord(i)-ord("a")]=1

def dfs(idx,cnt):
    global answer
    if k-5<0:
        return 0
    elif k==26:
        answer=n
        return n
    if cnt==k-5:
        readword=0
        for word in words:
            check=True
            for w in word:
                if alpha[ord(w)-ord("a")]==0:
                    check=False
                    break
            if check:
                readword+=1
        answer = max(answer,readword)
        return 

    for i in range(idx,26):
        if not alpha[i]:
            alpha[i]=1
            dfs(i,cnt+1)
            alpha[i]=0

dfs(0,0)
print(answer)
