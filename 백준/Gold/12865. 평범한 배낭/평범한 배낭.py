N, K = map(int, input().split())
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
wv = [[0,0]]
for _ in range(N):
    wv.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        w=wv[i][0]
        v=wv[i][1]
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(v+dp[i-1][j-w],dp[i-1][j])

print(dp[N][K])