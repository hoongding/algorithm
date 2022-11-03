# 부분문자열
# 문자의 순서는 뒤바뀔 수 없음.
# yxyc -> yyc가 제일 사전에서 뒤에 있는 문자열.

def solution(s):
    answer = ''
    stack_s = []
    for item in s:
        if len(stack_s) == 0:
            stack_s.append(item)

        elif stack_s[-1] < item:

            while stack_s:
                if stack_s[-1] < item:
                    stack_s.pop()
                    continue
                elif stack_s[-1] >= item:
                    stack_s.append(item)
                    break
            if stack_s:
                continue
            else:
                stack_s.append(item)
        elif stack_s[-1] >= item:
            stack_s.append(item)
    for item in stack_s:
        answer += item

    return answer