import sys
input = sys.stdin.readline

n = int(input())
dasom = int(input())
arr = [int(input()) for _ in range(n-1)]
cnt = 0
while True:
    if len(arr) == 0:
        print(0)
        break
    arr.sort(reverse=True)
    if dasom <= arr[0]:
        dasom += 1
        arr[0] -= 1
        cnt += 1

    else:
        print(cnt)
        break