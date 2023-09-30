from collections import defaultdict
def solution(phone_book):
    answer = True
    num_dic = defaultdict()
    for num in phone_book:
        num_dic[num] = len(num)
    for num in phone_book:
        answer = ''
        for i in num:
            answer += i
            if answer in num_dic and num!=answer:
                print("answer:",answer)
                return False
    return True