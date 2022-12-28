import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

grape_juice = [0]+[int(input()) for _ in range(n)]

if n >= 1:
    dp[1] = grape_juice[1]
if n >= 2:
    dp[2] = grape_juice[1]+grape_juice[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+grape_juice[i-1]+grape_juice[i],
                dp[i-2]+grape_juice[i], dp[i-1])

print(dp[n])
