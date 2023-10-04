n = int(input())
lst = list(map(int, input().split()))
target = 1
for i in range(n):
    target *= lst[i]

result = -1  # 초기값을 -1로 설정합니다.
result_arr = []

def dfs(product, arr):
    global target, result, result_arr
    if product > target:
        if result == -1 or sorted(arr) < sorted(result_arr):
            result = product
            result_arr = arr[:]
        return

    if len(arr) == n:
        return

    for i in range(1, 10):
        dfs(product * i, arr + [i])

dfs(1, [])
if result == -1:
    result_arr = [-1]

print(*result_arr)