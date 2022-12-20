import sys
input = sys.stdin.readline

sudokuList = [list(map(int, input().split())) for _ in range(1, 10)]
blankList = []
for i in range(9):
    for j in range(9):
        if sudokuList[i][j] == 0:
            blankList.append((i, j))


def checkRow(i, value):
    for k in range(9):
        if value == sudokuList[i][k]:
            return False
    return True


def checkCol(j, value):
    for k in range(9):
        if value == sudokuList[k][j]:
            return False
    return True


def checkSquare(i, j, value):
    nx = (i//3)*3
    ny = (j//3)*3
    for k in range(3):
        for h in range(3):
            if value == sudokuList[k+nx][h+ny]:
                return False
    return True


def dfs(idx):
    if idx == len(blankList):
        for i in range(9):
            print(*sudokuList[i])
        exit(0)
    for value in range(1, 10):
        i, j = blankList[idx]
        if checkRow(i, value) and checkCol(j, value) and checkSquare(i, j, value):
            sudokuList[i][j] = value
            dfs(idx+1)
            sudokuList[i][j] = 0


dfs(0)
