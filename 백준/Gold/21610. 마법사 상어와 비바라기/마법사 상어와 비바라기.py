import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dir = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]  # 현재 구름 위치
arrow_cr = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
            (0, 1), (1, 1), (1, 0), (1, -1)]
arr = []

for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)


def magic(d, s):
    global arr
    global dir
    dir_copy = []
    # 구름 d방향으로 s칸이동
    for x_cur, y_cur in dir:
        x = (x_cur+(arrow_cr[d][0]*s)) % n
        y = (y_cur+(arrow_cr[d][1]*s)) % n
        arr[x][y] += 1
        dir_copy.append((x, y))


    # 물복사버그 마법 시전
    for x_cur, y_cur in dir_copy:
        total = 0
        for j in range(4):
            arrow_c = arrow_cr[(j*2)+1]
            x = x_cur+arrow_c[0]
            y = y_cur+arrow_c[1]
            if x < n and y < n and x >= 0 and y >= 0 and arr[x][y] > 0:
                total += 1
        arr[x_cur % n][y_cur % n] += total

    dir = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in dir_copy:
                arr[i][j] -= 2
                dir.append((i, j))


def arr_sum(arr):
    total = 0
    for i in arr:
        total += sum(i)
    return total


for _ in range(m):
    d, s = map(int, input().split())
    magic(d-1, s)

print(arr_sum(arr))
