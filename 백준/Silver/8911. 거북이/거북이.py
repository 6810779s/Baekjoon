test_case = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(test_case):
    command = list(input())
    x = y = 0
    direction = 0
    path = [(x, y)]
    for c in command:
        if c == 'F':
            x += dx[direction]
            y += dy[direction]
        elif c == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif c == 'L':
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        elif c == 'R':
            if direction == 3:
                direction = 0
            else:
                direction += 1
        path.append((x, y))

    width = max(path, key= lambda x: x[0])[0] - min(path, key=lambda x: x[0])[0]
    height = max(path, key=lambda x: x[1])[1] - min(path, key=lambda x:x[1])[1]
    print(width*height)