import sys
inf = 1e19
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum_num = 0
max_num = 0

if N % 2 != 0:
    max_num = arr.pop()
for i in range(N//2):
    sum_num = max(arr.pop(0)+arr.pop(), sum_num)
sum_num = max(max_num, sum_num)
print(sum_num)