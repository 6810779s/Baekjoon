import sys

input = sys.stdin.readline

t = int(input())


def result(k, n):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            else:
                dp[i][j] = sum(dp[i-1][:j+1])

    print(dp[k][n])


for _ in range(t):
    k = int(input())
    n = int(input())
    result(k, n)