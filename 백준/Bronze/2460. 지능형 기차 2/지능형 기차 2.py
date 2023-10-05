result = 0
total = 0
for _ in range(10):
    off, on = map(int, input().split())
    total += on
    total -= off
    result = max(result, total)

print(result)