n = int(input())
lst = list(map(int,input().split()))
goal = int(input())
lst.sort()
left, right = 0, n-1
result=0
while left<right:
    total = lst[left]+lst[right]
    if total>goal:
        right-=1
    elif total==goal:
        result+=1
        left+=1
    else:
        left+=1
print(result)