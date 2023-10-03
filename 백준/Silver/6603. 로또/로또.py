result = []
def dfs(start, arr, k, lst, N):
    global result
    if len(arr)==N:
        result.append(arr)
        return
    for i in range(start, k):
        dfs(i+1, arr+[lst[i]], k, lst, N)


while True:
    lst = list(map(int, input().split()))
    if len(lst)==1 and lst[0] == 0:
        break
    result = []
    k = lst[0]
    lst = lst[1:]
    dfs(0, [], k, lst, 6)
    for row in sorted(result):
        print(*row)
    print()