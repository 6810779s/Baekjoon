import sys

input = sys.stdin.readline

phone1 = str(input())
phone2 = str(input())
# dp = [0 for _ in range(100)]
num = ""

for i in range(8):
    num = num+phone1[i]+phone2[i]

while len(num) > 2:
    dp = ""
    for i in range(1, len(num)):
        cal = (int(num[i-1])+int(num[i])) % 10
        dp += str(cal)
    num = dp

print(num)