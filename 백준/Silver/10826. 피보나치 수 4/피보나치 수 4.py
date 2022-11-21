import sys
input = sys.stdin.readline

n = int(input())


def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[num]


print(fibo(n))