import heapq
import sys
input = sys.stdin.readline
lst = []

n = int(input())
for _ in range(n):
    x=int(input())
    if x!=0:
        heapq.heappush(lst,(abs(x),x))
    else:
        if lst:
            print(heapq.heappop(lst)[1])
        else:
            print(0)