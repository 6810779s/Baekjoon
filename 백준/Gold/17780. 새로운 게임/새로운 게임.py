dx = [0, 0, -1, 1] #오른쪽, 왼쪽, 위, 아래
dy = [1, -1, 0, 0]

N, K = map(int, input().split())  # N: 체스판의 크기 , K: 말의 개수
# 0: 흰색, 1: 빨간색, 2: 파란색
board = [list(map(int,input().split())) for _ in range(N)]
white_board = [[[] for _ in range(N)] for _ in range(N)]

info = [[] for _ in range(K)]

for i in range(K):
    x, y, d = map(int, input().split())
    info[i] = [x-1, y-1, d-1] # 말 번호, 행, 열, 방향
    white_board[x - 1][y - 1].append(i) #i :말 번호, d: 말 방향
    

# 제일 밑에 말인지 확인 함수
def check_horse_pos(num, row, col):
    horse_state = white_board[row][col]
    if horse_state[0] == num:
        return True
    else:
        return False
    

# 방향 바꿔주는 함수
def reverse_d(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    elif d==3:
        return 2

# 방향을 바꿔도 파란색이나 범위 벗어났을 경우
def check_blue_again(row, col, d):
    rev_d = reverse_d(d)
    nx, ny = row + dx[rev_d], col + dy[rev_d]
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
        return True
    return False

# 다음 칸으로 말을 이동시키는 함수
def next_horse(row, col, d):
    nx, ny = row + dx[d], col + dy[d]
    # 범위 벗어나거나 파란색일 때
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
        if check_blue_again(row, col, d):
            return row,col,reverse_d(d)
        else:
            rev_d = reverse_d(d)
            return next_horse(row, col, rev_d)

    
    # 다음 칸이 빨간색 일 경우
    elif board[nx][ny] == 1:
        rev_horse_lst = white_board[row][col][::-1]

        for horse in rev_horse_lst:
            white_board[nx][ny].append(horse)

            row, col, h_d = info[horse] # d는 horse마다 다름
            info[horse] = [nx, ny, h_d] # 업데이트된 nx, nx를 넣어줌
        white_board[row][col] = []
    
    # 다음칸이 하얀색 일 경우
    elif board[nx][ny] == 0:
        # 다음칸에 말을 하나씩 올려줌
        for horse in white_board[row][col]:
            white_board[nx][ny].append(horse)
            row, col, h_d = info[horse]
            info[horse] = [nx, ny, h_d]
        white_board[row][col] = []  # 말이 이전에 있었던 칸 초기화

    return nx, ny, d

# 말 옮기기
def move_horses():
    for h in range(K):
        row,col,d = info[h]
        # 맨 밑일 떄
        if not check_horse_pos(h,row,col):
            continue
        nx,ny,nd = next_horse(row,col,d)
        info[h] = [nx,ny,nd]

# 말이 4개가 쌓여있다면
def check_horses_length():
    for i in range(N):
        for j in range(N):
            if len(white_board[i][j])>=4:
                return True
    return False

answer = -1
time = 1
while time <= 1000:
    move_horses()
    if check_horses_length():
        answer = time
        break
    time+=1


print(answer)
