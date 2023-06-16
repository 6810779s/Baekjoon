
def check_sosu(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True


def dfs(lst):
    if ''.join(lst) in result:
        return
    if len(lst)==N:
        result.add(''.join(lst))
        return
    for i in range(10):
        if check_sosu(int(''.join(lst+[str(i)]))):
            dfs(lst+[str(i)])
    

N = int(input())
sosu = [2,3,5,7]
result = set()
    
for i in sosu:
    if N<=1:
        result = sosu
    else:
        dfs([str(i)])

for num in sorted(list(result)):
    print(num)

