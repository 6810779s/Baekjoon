import sys
input = sys.stdin.readline

s = int(input())
sum = 0
i = 0
while sum <= s:
    i += 1
    sum += i
if sum > s:
    print(i-1)
else:
    print(i)

