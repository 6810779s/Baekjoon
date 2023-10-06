N = int(input())
stair = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N+1)]
if N<=2:
    print(sum(stair))
else:
    dp[1] = stair[0]
    dp[2] = dp[1] + stair[1]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-2]+stair[i-1], dp[i-2] + stair[i-1])
    print(dp[-1])