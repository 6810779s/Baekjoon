import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0, 0] for _ in range(7)]

for i in range(n):
    s, y = map(int, input().split())
    arr[y][s] += 1

cnt = 0
for i in arr:
    if i[0] % k == 0:
        cnt += i[0]//k
    else:
        cnt += (i[0]//k)+1

    if i[1] % k == 0:
        cnt += i[1]//k
    else:
        cnt += (i[1]//k)+1

print(cnt)
