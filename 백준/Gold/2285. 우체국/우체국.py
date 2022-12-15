import sys
input = sys.stdin.readline

n = int(input())
Xlst = []
total = 0
for i in range(n):
    X, A = map(int, input().split())
    total += A
    Xlst.append((X, A))

Xlst.sort(key=lambda x: x[0])

count = 0
for i, j in Xlst:
    count += j
    if count > (total/2):
        print(i)
        break
