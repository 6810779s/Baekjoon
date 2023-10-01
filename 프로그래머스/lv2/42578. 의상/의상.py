from collections import defaultdict


def solution(clothes):
    global arr
    answer = 1
    dress = defaultdict(int)
    for clothe in clothes:
        dress[clothe[1]] += 1
    
    for c in dress:
        answer*=(dress[c] + 1)
    return answer - 1
   