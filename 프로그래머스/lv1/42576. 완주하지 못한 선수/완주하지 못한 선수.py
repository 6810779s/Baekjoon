def solution(participant, completion):
    answer = ''
    dic_person = {}
    for p in participant:
        if p in dic_person:
            dic_person[p] += 1
        else:
            dic_person[p] = 1
            
    for p in completion:
        dic_person[p] -= 1
        
    for key in dic_person:
        if dic_person[key] != 0:
            answer = key
    return answer