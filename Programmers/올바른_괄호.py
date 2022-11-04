def solution(s):
    # "()()" 또는 "(())()" 는 올바른 괄호입니다.
    # ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
    answer = True
    temp = []
    for item in s:
        if item == '(':
            temp.append('(')
        if item == ')':
            if len(temp) == 0:
                return False
            elif temp.pop() == '(':
                continue
            else:
                return False
    if len(temp) > 0:
        return False

    return True