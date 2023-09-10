A, B = map(int,input().split()) # A:가로, B: 세로
N, M = map(int,input().split()) # N:로봇 개수 M:명령 개수

# [0, 0] : 로봇 종류, 로봇 방향
board = [[0 for _ in range(A)] for _ in range(B)]
dx = [-1, 0, 1, 0] # N, W, S, E
dy = [0, -1, 0, 1]
# 조건1 : 명령은 순차적으로 수행됨. 동시에 수행 불가능
# L: 왼쪽 90도, R: 오른쪽 90도, F: 앞으로 한 칸
robot_info = [[0,0,""] for _ in range(N+1)]
 

# 왼쪽 방향으로 90도 회전
def turn_left(direction):
    if direction=="N":
        return "W"
    elif direction=="W":
        return "S"
    elif direction=="S":
        return "E"
    elif direction=="E":
        return "N"

# 오른쪽 방향으로 90도 회전
def turn_right(direction):
    if direction=="N":
        return 'E'
    if direction=="W":
        return 'N'
    if direction=="S":
        return 'W'
    if direction=="E":
        return 'S'

def crash_wall_error(robot_num):
    return f'Robot {robot_num} crashes into the wall'

def crash_robot_error(robot1, robot2):
    return f'Robot {robot1} crashes into robot {robot2}'

def execute_command(r_num, r_c, r_repeat):
    for _ in range(r_repeat):
        if r_c=="L":
            robot_info[r_num][2] = turn_left(robot_info[r_num][2])
        elif r_c=="R":
            robot_info[r_num][2] = turn_right(robot_info[r_num][2])
        elif r_c=="F":
            cur_x, cur_y, cur_d = robot_info[r_num]
            if robot_info[r_num][2]=="N":
                nx = dx[0] + cur_x
                ny = dy[0] + cur_y
            elif robot_info[r_num][2]=="W":
                nx = dx[1] + cur_x
                ny = dy[1] + cur_y
            elif robot_info[r_num][2]=="S":
                nx = dx[2] + cur_x
                ny = dy[2] + cur_y
            elif robot_info[r_num][2]=="E":
                nx = dx[3] + cur_x
                ny = dy[3] + cur_y
            if not (0<=nx<B and 0<=ny<A):
                print(crash_wall_error(r_num))
                exit()
            elif board[nx][ny]:
                print(crash_robot_error(r_num, board[nx][ny]))
                exit()
            else:
                board[cur_x][cur_y] = 0
                board[nx][ny] = r_num
                robot_info[robot] = [nx,ny, cur_d]



for i in range(1,N+1):
    x, y, d = input().split()
    nx = B-int(y)
    ny = int(x) - 1
    robot_info[i] = [nx,ny,d]
    board[nx][ny] = i


for _ in range(M):
    robot, command, repeat = input().split()
    robot, repeat = int(robot),int(repeat)
    execute_command(robot, command, repeat)

print("OK")