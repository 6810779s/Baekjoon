import sys
from itertools import permutations
n, hp = map(int, input().split())


def time_dp(time, damage, dp):
    global limit
    idx = 0
    while idx < limit:
        if dp[idx] != 0:
            idx += 1
            continue
        dp[idx] = damage
        idx += time
    return dp


def res(dp, hp):
    cnt = 0
    # print("dp:", dp)
    for i in range(len(dp)):
        if hp <= 0:
            break
        hp -= dp[i]
        cnt += 1
    return cnt


total_time = 0
total_damage = 0

lst_t_d = []


for i in range(n):
    time, damage = map(int, input().split())
    total_time += time
    total_damage += damage
    lst_t_d.append((time, damage))


limit = total_time*((hp//total_damage)+1)
lst = list(permutations(lst_t_d, n))
result = 1e10
for i in range(len(lst)):
    dp = [0 for _ in range(total_time*((hp//total_damage)+1))]
    for t, d in lst[i]:
        dp = time_dp(t, d, dp)
    result = min(result, res(dp, hp))


print(result)
