H, W, X, Y = map(int, input().split())
B_arr = [list(map(int,input().split())) for _ in range(H+X)]
A_arr = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        A_arr[i][j]=B_arr[i][j]

for i in range(X,H):
    for j in range(Y, W):
        A_arr[i][j] = B_arr[i][j] - A_arr[i-X][j-Y]

for row in A_arr:
    print(*row)