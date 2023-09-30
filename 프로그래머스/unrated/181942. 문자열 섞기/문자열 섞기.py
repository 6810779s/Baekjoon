def solution(str1, str2):
    answer = ''.join(list(str1[i]+str2[i] for i in range(len(str1))))
    return answer