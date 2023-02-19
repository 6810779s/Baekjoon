lst = []
n = int(input())
idx_lst = list(map(int, input().split()))

for i in range(1, n+1):
    lst.insert(i-1-idx_lst[i-1], i)
print(*lst)