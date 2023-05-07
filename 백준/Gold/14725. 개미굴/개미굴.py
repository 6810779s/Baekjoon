class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):    
        cur = self.root
        for food in foods:
            if food not in cur:    #현재 탐색하는 층 안에 동일한 음식이 없을때
                cur[food] = {}
            cur = cur[food]    # 만약 A를 탐색 했다면 A의 children을 cur에 넣어서 탐색
        cur[0] = True
    
    def draw(self, deep, cur):    # 구조 그리기
        if 0 in cur:    #마지막 리프에 도달하면 반환
            return 
        cur_child = sorted(cur)    # 같은층에 여러 음식이 있을때는 사전순으로 정렬
        for child in cur_child:
            print("--"*deep + child)
            self.draw(deep+1,cur[child])

N = int(input())
trie = Trie()
for i in range(N):
    data = list(input().split())
    trie.add(data[1:])
trie.draw(0,trie.root)