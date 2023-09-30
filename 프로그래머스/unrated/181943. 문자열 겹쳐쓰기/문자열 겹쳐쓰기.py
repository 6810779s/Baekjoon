def solution(my_string, overwrite_string, s):
    length = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+length:]
    
    return answer