while True:
    string = input()
    if string == "R0C0":
        break
    R, C = string.replace("R", "").replace("C", " ").split()
    C = int(C)-1
    res = ""
    while C >= 0:
        res = chr((C % 26)+65)+res
        C = C//26-1
    print(res+R)