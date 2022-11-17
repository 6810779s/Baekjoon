import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

a = arr.pop()

while len(arr) > 0:
    b = arr.pop()
    if a < b:
        a, b = b, a
    cal = a+(b/2)
    a = cal

print(a)