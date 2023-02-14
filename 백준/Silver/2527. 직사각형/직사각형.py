def check_b():
    if (y1 == q2 and x2 < p1 and p2 > x1) or (x2 == p1 and q2 > y1 and y2 < q1) or (y2 == q1 and x2 < p1 and x1 < p2) or (x1 == p2 and q2 > y1 and y2 < q1):
        return True


def check_c():
    if (x1 == p2 and (y1 == q2 or q1 == y2)) or (p1 == x2 and (y1 == q2 or y2 == q1)) or (y1 == q2 and (p1 == x2 or p2 == x1)) or (q1 == y2 and (p1 == x2 or p2 == x1)):
        return True


def check_d():
    if x2 > p1 or y2 > q1 or p2 < x1 or q2 < y1:
        return True


for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if check_b():
        print("b")
    elif check_c():
        print("c")
    elif check_d():
        print("d")
    else:
        print("a")