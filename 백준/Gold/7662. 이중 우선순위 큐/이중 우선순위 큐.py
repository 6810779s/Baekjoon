# 똑같은 100이 두개 들어갔을 경우
# 하나만 삭제해도 방문처리가 되므로 나머지 하나도 없어짐
import heapq
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    k = int(input())
    q_max = []
    q_min = []
    visited = [False for _ in range(1000001)]
    for i in range(k):
        action, n = input().split()
        n = int(n)
        if action == "I":
            heapq.heappush(q_max, (-n, i))
            heapq.heappush(q_min, (n, i))
        elif action == "D" and n == -1:
            while q_min and visited[q_min[0][1]]:
                heapq.heappop(q_min)
            if q_min:
                visited[q_min[0][1]] = True
                heapq.heappop(q_min)
        elif action == "D" and n == 1:
            while q_max and visited[q_max[0][1]]:
                heapq.heappop(q_max)
            if q_max:
                visited[q_max[0][1]] = True
                heapq.heappop(q_max)

    while q_max and visited[q_max[0][1]]:
        heapq.heappop(q_max)
    while q_min and visited[q_min[0][1]]:
        heapq.heappop(q_min)

    if not q_max or not q_min:
        print("EMPTY")
    else:
        print(-heapq.heappop(q_max)[0], heapq.heappop(q_min)[0])
