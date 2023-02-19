def rec(lst, cnt):
    global res, res_lst
    if lst[-1] < 0:
        if res < cnt:
            res = cnt
            res_lst = lst[:-1]
        return
    return rec(lst+[lst[len(lst)-2]-lst[len(lst)-1]], cnt+1)


n = int(input())
res=0
res_lst = []
for i in range(n+1):
    rec([n, i], 0)
print(len(res_lst))
print(*res_lst)