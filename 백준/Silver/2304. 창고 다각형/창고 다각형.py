
n = int(input())
lst = []


for i in range(n):
    pos, height = map(int, input().split())
    lst.append([pos, pos+1, height])


lst.sort()
total = 0
while lst:
    min_height = 1e4+1
    idx = 0
    for i in range(len(lst)):
        if min_height > lst[i][2]:
            min_height = lst[i][2]
            idx = i
    width = abs(lst[0][0]-lst[-1][1])
    total += (width*min_height)
    for i in range(len(lst)):
        lst[i][2] -= min_height

    lst.pop(idx)
print(total)
