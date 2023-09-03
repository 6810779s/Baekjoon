import sys


# _, 오른, 왼, 위, 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 보드 크기, 말 개수
N, K = map(int, sys.stdin.readline().rstrip().split())
# 0: 흰, 1: 빨, 2: 파 -> 기록한 보드
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 말 위치 기록(겹쳐진 말 포함)
white_board = [[[] for _ in range(N)] for _ in range(N)]

# 말 번호 별 위치, 방향 기록할 배열
info = [[] for _ in range(K)]

for i in range(K):
    x, y, direction = map(int, sys.stdin.readline().rstrip().split())
    # 말 번호, 행, 열, 방향
    info[i] = [x - 1, y - 1, direction-1]
    # 말 위치 기록(겹쳐지게)
    white_board[x - 1][y - 1].append(i)


# 가장 밑에 있는 말인지 확인하는 함수 (이동시키려는 말이 가장 밑에 있어야 이동시킬 수 있음)
def check_horse_pos(num, row, col):
    horse_state = white_board[row][col]
    if horse_state[0] == num:
        return True
    else:
        return False


# 방향 반대로 바꾸는 함수
def reverse_d(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2


# 파란색이거나 벗어난 칸이라서 반대로 이동해봤는데 또 그런 상태인지 확인하는 함수
def check_blue_again(row, col, d):
    rev_d = reverse_d(d)
    nx,ny = row + dx[rev_d],col + dy[rev_d]
    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 2:
        return True
    return False


# 다음 칸으로 이동시키는 함수
def next_horse(row, col, d):
    nx, ny = row + dx[d], col + dy[d]

    # 다음 칸이 판을 벗어나는 경우 or 파란칸
    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 2:
        # 또 벗어나거나 파란칸이면 이동 안하고 방향만 반대로
        if check_blue_again(row, col, d):
            return row, col, reverse_d(d)
        else:
            rev_d = reverse_d(d)
            # 방향 바꿔서 이동한 칸의 색깔 별로 다시 처리해주기 위해 현재 함수 재귀 호출
            return next_horse(row, col, rev_d)

    # 다음 칸이 빨강칸
    elif board[nx][ny] == 1:
        # 말 반대로 바꿔줌
        rev_horse_list = white_board[row][col][::-1]
        # 말들 차례로 다음 칸에 올림
        for horse in rev_horse_list:
            white_board[nx][ny].append(horse)
            # 말들 정보 갱신
            row, col, h_d = info[horse]
            info[horse] = [nx, ny, h_d]
        # 이전 칸에 있던 말을 모두 옮겼으므로 빈 칸으로 만들어 줌
        white_board[row][col] = []
    # 다음 칸이 흰칸
    elif board[nx][ny] == 0:
        # 말들 차례로 다음 칸에 올림
        for horse in white_board[row][col]:
            white_board[nx][ny].append(horse)
            # 말들 정보 갱신
            row, col, h_d = info[horse]
            info[horse] = [nx, ny, h_d]
        # 이전 칸에 있던 말을 모두 옮겼으므로 빈 칸으로 만들어 줌
        white_board[row][col] = []

    return nx, ny, d


# 현재 턴에 모든 말들 이동시키는 함수
def move_horses():
    for h in range(K):
        row, col, d = info[h]
        # 말이 가장 밑이 아니면 다음 말로 넘어감
        if not check_horse_pos(h, row, col):
            continue

        # 현재 말 기준으로 옮기기 수행
        nx, ny, nd = next_horse(row, col, d)
        # 현재 말 정보 갱신
        info[h] = [nx, ny, nd]


# 게임이 끝날 수 있는지 확인하는 함수
def is_finish():
    for i in range(N):
        for j in range(N):
            if len(white_board[i][j]) >= 4:
                return True
    return False


# 게임 수행
answer = -1
time = 1
while time <= 1000:
    move_horses()
    if is_finish():
        answer = time
        break

    time += 1

print(answer)