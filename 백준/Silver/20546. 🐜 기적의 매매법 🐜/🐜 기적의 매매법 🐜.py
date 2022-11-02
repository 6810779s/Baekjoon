import sys

input = sys.stdin.readline
money = [int(input())]*2
stock_arr = list(map(int, input().split()))

bnp_stock = 0
timing_stock = 0

stock_price = []


def bnp(stock):  # money[0]
    global money
    stock_num = money[0]//stock
    money[0] = money[0]-(stock_num*stock)
    return stock_num


def check_arr(stock_price):
    if len(stock_price) == len(list(set(stock_price))):
        if max(stock_price) == stock_price[0] and min(stock_price) == stock_price[2]:
            return -1  # 내림차순
        elif max(stock_price) == stock_price[2] and min(stock_price) == stock_price[0]:
            return 1  # 오름차순
        else:
            return 0
    else:
        return 0


def timing(stock):  # money[1]
    global timing_stock
    stock_num = money[1]//stock
    if len(stock_price) == 3:
        res = check_arr(stock_price)
        if res == 1:
            money[1] = money[1]+(timing_stock*stock)
            stock_price.pop(0)
            stock_price.append(stock)
            return -1
        elif res == -1:
            money[1] = money[1]-(stock_num*stock)
            stock_price.pop(0)
            stock_price.append(stock)
            return stock_num
        stock_price.pop(0)
    stock_price.append(stock)
    return 0


for i in range(len(stock_arr)):
    bnp_stock += bnp(stock_arr[i])
    timing_stock_num = timing(stock_arr[i])
    if timing_stock_num == -1:
        timing_stock = 0
    else:
        timing_stock += timing_stock_num

bnp_total = money[0]+(bnp_stock*stock_arr[-1])
timing_total = money[1]+(timing_stock*stock_arr[-1])
if bnp_total > timing_total:
    print("BNP")
elif bnp_total < timing_total:
    print("TIMING")
else:
    print("SAMESAME")
