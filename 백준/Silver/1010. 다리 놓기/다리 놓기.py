import sys
input = sys.stdin.readline

t = int(input())


def factorial(num):
    if num <= 1:
        return 1
    dp = [0 for _ in range(num+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, num+1):
        dp[i] = dp[i-1]*i
    return dp[num]


def cases(n, m):
    parent1 = factorial(m-n)
    parent2 = factorial(n)
    son = factorial(m)
    return int(son/(parent1*parent2))


for _ in range(t):
    n, m = map(int, input().split())
    print(cases(n, m))
