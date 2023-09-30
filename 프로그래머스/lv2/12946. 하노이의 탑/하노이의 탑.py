def hanoi(start, to, mid, num, answer):
    if num == 1:
        answer.append([start, to])
        return answer
    hanoi(start, mid, to, num-1, answer)
    answer.append([start, to])
    hanoi(mid, to, start,num-1, answer)
def solution(n):
    answer = []
    hanoi(1, 3, 2, n, answer)
    return answer