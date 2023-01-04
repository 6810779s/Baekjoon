n, k = map(int, input().split())  #학생 수, 한 방 최대 인원 수
female = [0] * 1000
male = [0] * 1000

for j in range(n):
    s, y = map(int, input().split())  #성별, 학년
    #학년별 인원수 체크
    if s == 0:  #여자
        female[y] += 1
    else:  #남자
        male[y] += 1
    
for j in range(1, 7):
    if female[j] % k == 0:  #인원수 딱 맞게 떨어질 때
        female[j] = female[j] // k
    else:
        female[j] = (female[j] // k) + 1

    if male[j] % k == 0:
        male[j] = male[j] // k
    else:
        male[j] = (male[j] // k) + 1

print(sum(female) + sum(male))