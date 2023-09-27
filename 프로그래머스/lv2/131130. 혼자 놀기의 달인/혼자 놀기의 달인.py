def solution(cards):
    answer = 0
    n = len(cards)
    visited = [False for _ in range(n)]
    res=[]
    for i in range(n):
        if not visited[i]:
            num = i
            cnt = 0
            while not visited[num]:
                visited[num] = True
                num = cards[num] - 1
                cnt+=1
            res.append(cnt)
    res.append(0)
    res = sorted(res, reverse = True)
    
    return res[0] * res[1]