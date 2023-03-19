import sys
import math
input=sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
total = []
for i in range(k, n+1):  # 3, 4, 5
    for j in range(n-i+1):  # i = 3, j=0, 1, 2
        ave = sum(lst[j:j+i])/i
        cal = 0
        for h in range(j, j+i):
            cal += (lst[h]-ave)**2
        res = cal/i
        total.append(res)
print(math.sqrt(min(total)))
