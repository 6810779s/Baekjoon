import sys
input = sys.stdin.readline
import heapq
n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            ab, res = heapq.heappop(heap)
            print(res)
        else:
            print(0)