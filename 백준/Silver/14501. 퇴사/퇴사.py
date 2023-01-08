import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(t+2)]

for i in range(1, t+1):
    date, money = map(int, input().split())
    if i+date < t+2:
        for j in range(i+date, t+2):
            dp[j] = max(dp[i]+money, dp[j])


print(max(dp))
