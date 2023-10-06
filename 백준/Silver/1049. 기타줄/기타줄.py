N, M = map(int, input().split())
limit = 5001
dp = [float('INF') for _ in range(limit)]


for _ in range(M):
    package_price, per_price = map(int, input().split())
    for i in range(6, limit, 6):
        dp[i] = min((i//6) * package_price, dp[i])

    for i in range(1,limit):
        dp[i] = min(dp[i], dp[i-1]+per_price, per_price * i)

print(min(dp[N:]))