def paint(l_x, l_y, r_x, r_y):
    cnt = 0
    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            if board[i][j] == 1:
                continue
            board[i][j] = 1
            cnt += 1
    return cnt


total = 0
board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    total += paint(lx, ly, rx, ry)
print(total)