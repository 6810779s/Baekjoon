import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def cal(num1, num2):
    cnt = 2
    min_num = 1
    max_num = 1
    while cnt <= min(num1, num2):
        if num1 % cnt == 0 and num2 % cnt == 0:
            num1 /= cnt
            num2 /= cnt
            min_num *= cnt
        else:
            cnt += 1

    return [min_num, int(min_num*num1*num2)]


[min_num, max_num] = cal(n, m)
print(min_num)
print(max_num)