
def attack_domino(x,y,d):
    global board,result_board,score
    if result_board[x][y]=='S':
        cnt = board[x][y]
        
        while cnt:
            if x<0 or x>=N or y<0 or y>=M:
                break
            if result_board[x][y]=='S':
                cnt = max(cnt,board[x][y])
                result_board[x][y]='F'
                score+=1
            x+=dx[d]
            y+=dy[d]
            cnt-=1
  
            


def defense_demino(x,y):
    global board,result_board
    if result_board[x][y]=='F':
        result_board[x][y]='S'


score=0
N, M, R = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result_board = [['S' for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
attack=[]
defense=[]
for i in range(R*2):
    if i%2: #방어
        X,Y = map(int,input().split())
        defense_demino(X-1,Y-1)
    else: # 공격
        X,Y,D = input().split()
        direction=0
        if D=='E':
            direction=0
        elif D=='W':
            direction=1
        elif D=='S':
            direction=2
        elif D=='N':
            direction=3
        attack_domino(int(X)-1,int(Y)-1,direction)


print(score)
for row in result_board:
    print(*row)
