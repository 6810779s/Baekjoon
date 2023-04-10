N,M=map(int,input().split())
wood=list(map(int,input().split()))
l,r=1,max(wood)
res=0
while l<=r:
    mid = (l+r)//2
    total = sum(list(i-mid for i in wood if i>mid))
    if total>=M:
        l=mid+1
    else:
        r=mid-1
print(r)