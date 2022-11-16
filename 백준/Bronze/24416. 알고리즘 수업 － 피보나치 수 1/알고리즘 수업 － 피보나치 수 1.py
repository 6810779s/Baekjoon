import sys
input = sys.stdin.readline

n = int(input())

cnt = [0, 0]


def fib(n):
    global cnt

    if n == 1 or n == 2:
        return 1
    cnt[0] += 1
    return fib(n-1)+fib(n-2)


def fibonacci(n):
    global cnt
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        cnt[1] += 1
        dp[i] = dp[i-1]+dp[i-2]


fib(n)
fibonacci(n)

print(cnt[0]+1, cnt[1])