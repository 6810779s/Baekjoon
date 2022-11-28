import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]


arr.sort(key=lambda x: (x[1], x[0]))
last = -1
cnt = 0
for start, end in arr:
    if start >= last:
        last = end
        cnt += 1


print(cnt)
