n = int(input())
lst = list(map(int, input().split()))
lst.sort()
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = dp[i-1]+lst[i-1]
print(sum(dp))