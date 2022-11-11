# 문자열에서 같은 알파벳이 2개 붙어있는 짝을 찾는다.
# 둘을 제거한 뒤 앞뒤로 문자열을 이어 붙인다.
# 다 제거할 수 있으면 1
# 아니면 0

def solution(s):
    stack_s = []
    for item in s:
        if len(stack_s) == 0:
            stack_s.append(item)
        elif stack_s[-1] == item:
            stack_s.pop()
        else:
            stack_s.append(item)
    if stack_s:
        return 0
    else:
        return 1


