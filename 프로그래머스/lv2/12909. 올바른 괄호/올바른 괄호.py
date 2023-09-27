def solution(s):
    answer = True
    stack = []
    for sign in s:
        if sign=='(':
            stack.append(sign)
        else:
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True