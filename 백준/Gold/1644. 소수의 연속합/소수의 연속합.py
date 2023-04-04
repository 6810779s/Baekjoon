import sys
input=sys.stdin.readline
def sosu(num):
    if num<=1:
        return 0
    elif num==2:
        return 1
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1

n = int(input())

sosu_lst=[]
for i in range(n+1):
    if sosu(i):
        sosu_lst.append(i)
r=0
total = 0
cnt=0
for l in range(len(sosu_lst)):
    while total<n and r<len(sosu_lst):
        total+=sosu_lst[r]
        r+=1
    if total==n:
        cnt+=1
    total-=sosu_lst[l]

print(cnt)

