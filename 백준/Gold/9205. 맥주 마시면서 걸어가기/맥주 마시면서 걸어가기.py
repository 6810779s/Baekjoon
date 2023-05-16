from collections import deque

def bfs(cx,cy):
    q = deque([(cx,cy)])

    while q:
        x,y = q.popleft()
        if abs(x-ex)+abs(y-ey)<=1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i] and abs(x-conv_lst[i][0])+abs(y-conv_lst[i][1])<=1000:
                visited[i]=True
                q.append((conv_lst[i][0],conv_lst[i][1]))
    print("sad")
    return


t = int(input())
for tc in range(t):
    n = int(input())
    visited=[False for _ in range(n)]
    conv_lst=[]
    points_lst=[]
    for i in range(n+2):
        x,y = map(int,input().split())
        if i==0 or i==n+1:
            points_lst.extend([x,y])
        else:
            conv_lst.append((x,y))
    sx,sy,ex,ey = points_lst
    bfs(sx,sy)