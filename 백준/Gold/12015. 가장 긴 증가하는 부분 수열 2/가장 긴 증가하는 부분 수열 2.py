n = int(input())
num_lst = list(map(int, input().split()))

stack = [0]

for i in num_lst:
    if stack[-1]<i:
        stack.append(i)
    else:
        s,e=0,len(stack)-1
        while s<=e:
            mid=(s+e)//2
            if i<stack[mid]:
                e = mid-1
            elif i==stack[mid]:
                s=mid
                break
            else:
                s = mid+1
        stack[s]=i
print(len(stack)-1)