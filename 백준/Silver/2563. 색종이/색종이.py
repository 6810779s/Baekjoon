def paint(cur_x, cur_y):
    cnt = 0
    for i in range(cur_x, cur_x+10):
        for j in range(cur_y, cur_y+10):
            if board[i][j] == 1:
                continue
            board[i][j] = 1
            cnt += 1
    return cnt


total = 0
n = int(input())
board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    total += paint(b, a)
print(total)