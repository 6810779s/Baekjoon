N = int(input())
K = int(input())
board=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1


L = int(input())
dx = [1, 0, -1, 0]  # 0 아래, 1 왼쪽, 2 위, 3 오른쪽
dy = [0, -1, 0, 1]

x = 0
y = 0 # 뱀 머리 좌표
board[x][y] = 2 # 뱀 표시
result = 0
direction = 3
snake_body = [(0, 0)]
time_dic = {}
for _ in range(L):
    X, C = input().split()
    time_dic[int(X)] = C

while True:
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < N and 0 <= ny <N:
        if board[nx][ny] == 1: # 사과 먹었을때
            snake_body.append((nx, ny))
            board[nx][ny] = 2
            x, y = nx, ny
        elif board[nx][ny] == 0: # 사과 안먹고 앞으로 전진만
            s_x, s_y = snake_body.pop(0) # 뱀꼬리
            board[s_x][s_y] = 0 
            x, y = nx, ny # 뱀 머리
            snake_body.append((nx, ny))
            board[nx][ny] = 2
        else: # 자기몸 닿았을때
            break
    else:
        break
    result += 1
    if result in time_dic:
        if time_dic[result] == "L":  # 왼쪽
            if direction == 0:
                direction = 3
            else:
                direction -= 1 
        elif time_dic[result] == "D":  # 오른쪽
            direction = (direction + 1) % 4


print(result + 1)