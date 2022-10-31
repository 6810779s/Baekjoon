import sys
inf = 1e9
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [inf]*(c+100)
dp[0]=0
for _ in range(n):
    cost, client = map(int, input().split())

    for i in range(client, c+100):
        dp[i] = min(dp[i], dp[i-client]+cost)
    

print(min(dp[c:]))