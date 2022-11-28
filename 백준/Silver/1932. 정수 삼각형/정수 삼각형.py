import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.reverse()

for i in range(1, n):
    for j in range(len(arr[i])):
        arr[i][j] = max(arr[i-1][j], arr[i-1][j+1])+arr[i][j]

print(arr[-1][-1])
