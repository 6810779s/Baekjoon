import sys
input = sys.stdin.readline

test_answer = list(map(int, input().split()))
res = 0


def dfs(num, sheet):
    global res
    if num == 10:
        point = 0
        for i in range(10):
            if test_answer[i] == sheet[i]:
                point += 1
            if point == 5:
                res += 1
                break
        return

    for i in range(1, 6):
        if len(sheet) > 1 and sheet[num-2] == sheet[num-1] == i:
            continue

        sheet.append(i)
        dfs(num+1, sheet)
        sheet.pop()


dfs(0, [])
print(res)