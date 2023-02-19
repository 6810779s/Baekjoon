def paint(cur_x, cur_y, cur_w, cur_h):
    cnt = 0
    for i in range(cur_x, cur_h+cur_x):
        for j in range(cur_y, cur_w+cur_y):
            if board[i][j] == 1:
                continue
            board[i][j] = 1
            cnt += 1
    return cnt


n = int(input())
board = [[0 for _ in range(1001)] for _ in range(1001)]
lst = []
for _ in range(n):
    total = 0
    x, y, w, h = map(int, input().split())
    lst.append((x, y, w, h))
lst.reverse()

res = []
for x, y, w, h in lst:
    cnt = paint(y, x, w, h)
    res.append(cnt)

for i in range(len(res)-1, -1, -1):
    print(res[i])