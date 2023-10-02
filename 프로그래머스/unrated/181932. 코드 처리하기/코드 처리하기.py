def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i]=='1':
            mode = (mode+1)%2
            continue
        if mode:
            if i%2:
                answer += code[i]
        else:
            if not i%2:
                answer += code[i]
    return answer if answer else 'EMPTY'