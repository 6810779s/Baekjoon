from collections import deque

num_arr = deque(list(range(1, int(input())+1)))

while len(num_arr)>1:

    num_arr.popleft()
    num = num_arr.popleft()
    num_arr.append(num)


print(num_arr[0])