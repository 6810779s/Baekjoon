import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+2)]

max_num = 0
for i in range(1, n+1):
    days, money = map(int, input().split())
    max_num = max(dp[i], max_num)

    if i+days > n+1:  # 1~8
        continue

    dp[i+days] = max(max_num+money, dp[i+days])


print(max(dp))