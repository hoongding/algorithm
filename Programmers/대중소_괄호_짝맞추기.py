def solution(s):
    answer = True
    stack = []
    for item in s:
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
        else:
            if len(stack) == 0:
                return False

            if item == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif item == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif item == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    else:
        return True

