def check(lst):
    idx = 1
    cur_x, cur_y = h, 0
    dir = 0
    while idx != n+1:
        nx, ny = d[dir][0]+cur_x, d[dir][1]+cur_y
        if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == 0:
            lst[nx][ny] = idx
            idx += 1
            cur_x, cur_y = nx, ny
            continue

        dir = (dir+1) % 4

    return cur_y+1, h-cur_x


d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
w, h = map(int, input().split())
lst = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

if n > w*h:
    print(0)
else:
    x, y = check(lst)
    print(x, y)