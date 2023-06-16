def check_board(x,y):
    for i in range(4):
        cur_x, cur_y = x,y
        while True:
            nx,ny = dx[i]+cur_x, dy[i]+cur_y
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]=='S':
                    return False
                elif board[nx][ny]=='O' or board[nx][ny]=='T':
                    break
                else:
                    cur_x, cur_y = nx,ny
            else:
                break
    return True
                
                


def dfs(cnt):
    if cnt==3:
        flag = True
        for x,y in teacher:
            if not check_board(x,y):
                flag = False
                break
        if flag:
            print("YES")
            exit()
        return
    for i in range(N):
        for j in range(N):
            if board[i][j]=='X':
                board[i][j]='O'
                dfs(cnt+1)
                board[i][j]='X'
                




cnt = 0
N = int(input())
teacher = []
board = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(N):
    lst = list(input().split())
    for j in range(N):
        if lst[j]=="T":
            teacher.append((i,j))
    board.append(lst)

dfs(0)
print("NO")
