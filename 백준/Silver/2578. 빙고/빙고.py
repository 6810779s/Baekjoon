def check(num):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == num:
                bingo_board[i][j] = 0
                return


def check_row_col(board):
    cnt = 0
    for row in board:
        if sum(row) == 0:
            cnt += 1
    return cnt


def check_left_right(board):
    cnt = 0
    total = 0
    for i in range(5):
        if total > 0:
            break
        for j in range(5):
            if i == j:
                total += board[i][j]

    if total == 0:
        cnt += 1
    return cnt


def check_right_left(board):
    cnt = 0
    total = 0
    for i in range(5):
        if total > 0:
            break
        for j in range(5):
            if i+j == 4:
                total += board[i][j]

    if total == 0:
        cnt += 1
    return cnt


def res_bingo():
    cnt = 0
    for row in bingo:
        res = 0
        for i in range(5):
            res = 0
            cnt += 1
            check(row[i])
            res += check_row_col(bingo_board)
            res += check_row_col(list(zip(*bingo_board)))
            res += check_left_right(bingo_board)
            res += check_right_left(bingo_board)

            if res >= 3:
                print(cnt)
                return


bingo_board = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]
res_bingo()