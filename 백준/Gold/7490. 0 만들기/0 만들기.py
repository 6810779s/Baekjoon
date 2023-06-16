def cal_num(num_str):
    num_lst = []
    sign_lst=[]
    
    for s in num_str:
        if s=='+' or s=='-' or s==' ':
            sign_lst.append(s)
        else:
            if sign_lst and sign_lst[-1]==' ':
                sign_lst.pop()
                num = num_lst.pop()
                num_lst.append(num*10+int(s))
            else:
                num_lst.append(int(s))
    while sign_lst:
        num1 = num_lst.pop(0)
        num2 = num_lst.pop(0)
        sign = sign_lst.pop(0)
        if sign=='+':
            num_lst.insert(0,num1+num2)
        else:
            num_lst.insert(0,num1-num2)
    if num_lst[0]==0:
        return True
    else:
        return False


def dfs(n,cal,depth):
    global result
    if depth==n:
        if cal_num(cal):
            result.append(cal)
        return
    for s in sign:
        dfs(n, cal+s+str(depth+1),depth+1)



T = int(input())


result = []
sign = ['+', '-',' ']
for i in range(T):
    n = int(input())
    dfs(n,'1',1,)
    result.sort()
    for row in result:
        print(row)
    if i!=T-1:
        print()
    result = []