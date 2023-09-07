from collections import deque

n, w, L = map(int, input().split())
truck_lst = deque(list(map(int,input().split())))
route_q = deque([0 for _ in range(w)])

time = 0
def check_weight(t_w):
    return L>=t_w+sum(route_q)


while truck_lst:
    route_q.popleft()
    if check_weight(truck_lst[0]):
        truck = truck_lst.popleft()
        route_q.append(truck)
    else:
        route_q.append(0)
    time+=1
    
last_truck = 0
for i in range(len(route_q)-1,-1,-1):
    if route_q[i]!=0:
        last_truck = i
        break
    


print(time+last_truck+1)