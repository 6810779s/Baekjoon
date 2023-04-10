def check_sosu(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def check_palindrome(num):
    num_lst=list(str(num))
    if num_lst==num_lst[::-1]:
        return True
    return False

N=int(input())
res=0
for i in range(N,1000001):
    if i==1:
        continue
    if check_sosu(i) and check_palindrome(i):
        res=i
        break
if res==0:
    res=1003001
print(res)