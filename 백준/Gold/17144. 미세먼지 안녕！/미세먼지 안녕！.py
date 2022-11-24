import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

visited = [[False for _ in range(c)] for _ in range(r)]
dx = [(0, -1), (0, 1), (1, 0), (-1, 0)]
topStartIdx = 0
bottomStartIdx = 0
for i in range(r):
    if arr[i][0] == -1:
        topStartIdx = i
        bottomStartIdx = i+1
        break


def clean():
    global arr
    arr_copy = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                for a, b in dx:
                    nx = i+a
                    ny = j+b

                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        arr_copy[nx][ny] += arr[i][j]//5
                        cnt += 1

                arr_copy[i][j] = arr_copy[i][j] + \
                    arr[i][j]-(arr[i][j]//5*cnt)
            elif arr[i][j] == -1:
                arr_copy[i][j] = -1
    arr = arr_copy[:]


def activeTop():
    global arr, topStartIdx
    dn = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pre_num = 0
    i = topStartIdx
    j = 0
    n = 0
    while True:
        dx = i+dn[n][0]
        dy = j+dn[n][1]
        if dx == topStartIdx and dy == 0:
            break
        if dx < 0 or dx > r-1 or dy < 0 or dy > c-1:
            n += 1
            continue
        pre_num, arr[dx][dy] = arr[dx][dy], pre_num
        i = dx
        j = dy


def activeBottom():
    global arr, bottomStartIdx
    dn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pre_num = 0
    i = bottomStartIdx
    j = 0
    n = 0
    while True:
        dx = i+dn[n][0]
        dy = j+dn[n][1]
        if dx == bottomStartIdx and dy == 0:
            break
        if dx < 0 or dx > r-1 or dy < 0 or dy > c-1:
            n += 1
            continue
        pre_num, arr[dx][dy] = arr[dx][dy], pre_num
        i = dx
        j = dy


total = 0
for _ in range(t):
    clean()
    activeTop()
    activeBottom()


for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            total += arr[i][j]

print(total)
