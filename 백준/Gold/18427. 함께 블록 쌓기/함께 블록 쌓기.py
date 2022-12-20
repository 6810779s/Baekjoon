import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

dp = [[1]+[0 for _ in range(h)] for _ in range(n+1)]


for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    blockLst = list(map(int, input().split()))
    for b in blockLst:
        for k in range(b, h+1):
            dp[i][k] += dp[i-1][k-b]

print(dp[n][h] % 10007)
