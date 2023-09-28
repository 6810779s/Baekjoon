from collections import defaultdict
def solution(record):
    answer = []
    result = []
    nickname_name = {}
    for i in record:
        s_lst = i.split()
        if s_lst[0] =='Enter':
            nickname_name[s_lst[1]] = s_lst[2]
            answer.append(('들어왔습니다.', s_lst[1]))
        elif s_lst[0] == 'Leave':
            answer.append(('나갔습니다.', s_lst[1]))
        else:
            nickname_name[s_lst[1]] = s_lst[2]
    for state, user_id in answer:
        result.append(f"{nickname_name[user_id]}님이 {state}")
    
    return result
