n = int(input())
cal_lst = list(input())
result = -int(1e9)

def cal(n1, n2, op):
    n1=int(n1)
    n2=int(n2)
    if op=="+":
        return n1+n2
    elif op=="*":
        return n1*n2
    elif op=="-":
        return n1-n2

def dfs(idx, prev):
    global result
    if idx>=n:
        result = max(result, prev)
        return 
    if idx+3<n:
        dfs(idx+4, cal(prev, cal(cal_lst[idx+1],cal_lst[idx+3],cal_lst[idx+2]),cal_lst[idx]))
    dfs(idx+2, cal(prev,cal_lst[idx+1],cal_lst[idx]))

if n==1:
    result = cal_lst[0]
else:
    dfs(1, cal_lst[0])

print(result)