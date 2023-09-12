def find_parent(a):
    result = [a]
    while parent[a]:
        result.append(parent[a])
        a = parent[a]
    return result


T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N + 1)]
    for _ in range(N-1):
        A, B = map(int,input().split()) # A가 B의 부모
        parent[B] = A  # 자기의 부모 추가
    find_p1, find_p2 = map(int,input().split())
    p_1 = find_parent(find_p1)
    p_2 = find_parent(find_p2)
    i = j = 0
    if len(p_1) > len(p_2) : 
        i = len(p_1) - len(p_2)
    else:
        j = len(p_2) - len(p_1)
    while p_1[i] != p_2[j]:
        i+=1
        j+=1
    print(p_1[i])
