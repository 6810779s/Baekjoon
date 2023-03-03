n = int(input())
k = int(input())
s = 0
e = k
res = 0


while s < e:
    m = (s+e)//2
    total = 0
    for i in range(1, n+1):
        total += min(m//i, n)
    if total < k:
        s = m+1
    else:
        e = m
print(s)