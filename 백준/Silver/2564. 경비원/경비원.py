def cal(pos, x):
    if pos == 1:
        return -x
    elif pos == 2:
        return h+x
    elif pos == 3:
        return x
    elif pos == 4:
        return -(w+x)


w, h = map(int, input().split())
n = int(input())
store = []
for _ in range(n+1):
    a, b = map(int, input().split())
    store.append(cal(a, b))
total = 0
for i in range(n):
    num = abs(store[-1]-store[i])
    num1 = 2*(w+h)-num
    total += min(num, num1)
print(total)