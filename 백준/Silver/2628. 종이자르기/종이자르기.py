w, h = map(int, input().split())
n = int(input())

w_lst = [0]
h_lst = [0]
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        h_lst.append(b)
    else:
        w_lst.append(b)

w_lst.sort()
h_lst.sort()
w_lst += [w]
h_lst += [h]
max_w = 0
max_h = 0
for i in range(1, len(w_lst)):
    max_w = max(max_w, w_lst[i]-w_lst[i-1])

for i in range(1, len(h_lst)):
    max_h = max(max_h, h_lst[i]-h_lst[i-1])

print(max_w*max_h)