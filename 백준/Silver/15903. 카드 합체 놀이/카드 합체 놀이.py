import sys
import heapq
input=sys.stdin.readline

n, m = map(int, input().split())
heap = []
card = list(map(int, input().split()))
for c in card:
    heapq.heappush(heap, c)
cnt = 0
while cnt < m:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    heapq.heappush(heap, num1+num2)
    heapq.heappush(heap, num1+num2)
    cnt += 1

print(sum(heap))
