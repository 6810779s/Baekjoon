import copy
# def check_d(x,y,di):
#     n = len(cctv_d[di-1])
#     d_lst = [0 for _ in range(n)]
#     for dx in range(n):
#         nx,ny = x+d[cctv_d[di-1][dx]][0],y+d[cctv_d[di-1][dx]][1]
#         length = 0
#         while 0<=nx<N and 0<=ny<M:
#             if board[nx][ny]==6:
#                 break
#             length+=1
#             nx+=d[cctv_d[di-1][dx]][0]
#             ny+=d[cctv_d[di-1][dx]][1]
#         d_lst[dx]=length
#     return d_lst
    
def watch(x,y,dx,board):
    global res
    for i in dx:
        nx,ny = x,y
        while True:
            nx,ny = nx+d[i][0], ny+d[i][1]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==6:
                    break
                elif board[nx][ny]==0:
                    board[nx][ny]="#"
            else:
                break

def dfs(depth, board):
    global res
    if depth==len(cctv):
        res=min(cnt_zero(board), res)
        return
    
    x,y,di = cctv[depth]
    copy_board = copy.deepcopy(board)
    # direction = check_d(x,y,di)
    for dx in cctv_d[di-1]:
        watch(x,y,dx,copy_board)
        dfs(depth+1,copy_board)
        copy_board=copy.deepcopy(board)

def cnt_zero(lst):
    cnt=0
    for i in range(N):
        for j in range(M):
            if lst[i][j]==0:
                cnt+=1
    return cnt
d = [(0,1),(0,-1),(1,0),(-1,0)]    # 0우, 1좌, 2하, 3상
cctv_d = [[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,3],[0,2],[1,2],[1,3]],[[0,1,3],[0,2,3],[0,1,2],[1,2,3]],[[0,1,2,3]]]


N,M = map(int,input().split())
res = (N*M)+1
space = N*M
board = []
cctv=[]
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(M):
        if row[j]!=0 and row[j]!=6:
            cctv.append((i,j,row[j]))
            space-=1
    board.append(row)


dfs(0,board)
print(res)