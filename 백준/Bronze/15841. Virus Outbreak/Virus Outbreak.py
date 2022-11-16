def fib(n):
    if n == 1 or n == 2:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


while True:
    num = int(input())
    if num == -1:
        break
    print('Hour %d: %d cow(s) affected' % (num, fib(num)))