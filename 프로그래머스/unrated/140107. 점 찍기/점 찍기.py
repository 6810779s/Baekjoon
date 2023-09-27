from itertools import permutations



def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        max_num = int((d**2 - i**2) **0.5)
        answer += (max_num // k) + 1

    
    return answer