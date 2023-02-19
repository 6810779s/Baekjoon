def check(num):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == num:
                bingo_board[i][j] = 0
                return


def check_row():
    cnt = 0
    for row in bingo_board:
        if sum(row) == 0:
            cnt += 1
    return cnt


def check_col():
    cnt = 0
    for i in range(5):
        total = 0
        for j in range(5):
            total += bingo_board[j][i]
            if total > 0:
                break
        if total == 0:
            cnt += 1
    return cnt


def check_left_right():
    cnt = 0
    total = 0
    for i in range(5):
        if total > 0:
            break
        for j in range(5):
            if i == j:
                total += bingo_board[i][j]

    if total == 0:
        cnt += 1
    return cnt


def check_right_left():
    cnt = 0
    total = 0
    for i in range(5):
        if total > 0:
            break
        for j in range(5):
            if i+j == 4:
                total += bingo_board[i][j]

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
            res += check_row()
            res += check_col()
            res += check_left_right()
            res += check_right_left()

            if res >= 3:
                print(cnt)
                return


bingo_board = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]
res_bingo()