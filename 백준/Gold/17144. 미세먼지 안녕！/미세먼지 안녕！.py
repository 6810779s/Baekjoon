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

                    if 0 <= nx < r and 0 <= ny < c:
                        if arr[nx][ny] != -1:
                            arr_copy[nx][ny] += arr[i][j]//5
                            cnt += 1

                arr_copy[i][j] = arr_copy[i][j] + \
                    arr[i][j]-(arr[i][j]//5*cnt)
            elif arr[i][j] == -1:
                arr_copy[i][j] = -1
    arr = arr_copy


def activeTop():
    global arr, topStartIdx

    # top
    i = topStartIdx
    j = 0
    pre_num = 0

    while True:

        if i == topStartIdx and j != c-1:
            j += 1
        elif 0 < i <= topStartIdx and j == c-1:
            i -= 1
        elif i == 0 and j != 0:
            j -= 1
        elif 0 <= i < topStartIdx and j == 0:
            i += 1
        pre_num, arr[i][j] = arr[i][j], pre_num
        if i == topStartIdx and j == 0:
            arr[i][j] = -1
            break


def activeBottom():
    global arr, bottomStartIdx
    # bottom
    i = bottomStartIdx
    j = 0
    pre_num = 0
    while True:
        if i == bottomStartIdx and j != c-1:
            j += 1
        elif bottomStartIdx <= i < r-1 and j == c-1:
            i += 1
        elif i == r-1 and j != 0:
            j -= 1
        elif bottomStartIdx < i <= r-1 and j == 0:
            i -= 1

        pre_num, arr[i][j] = arr[i][j], pre_num
        if i == bottomStartIdx and j == 0:
            arr[i][j] = -1
            break


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
