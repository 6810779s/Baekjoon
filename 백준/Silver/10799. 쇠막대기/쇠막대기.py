bar_lst = list(input())
bar = 1
total = 0
stack = [bar_lst[0]]


for i in range(1,len(bar_lst)):
    if bar_lst[i]=="(":
        bar+=1
        stack.append("(")
    else:
        if bar_lst[i-1]=="(":
            stack.pop()
            bar-=1
            total+=bar
        else:
            if stack and stack[-1]=="(":
                stack.pop()
                total+=1
                bar-=1

print(total)