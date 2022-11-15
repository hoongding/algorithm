# 빵 야채 고기 빵 순서로 쌓인 햄버거만 포장함.
# return : 포장할 수 있는 햄버거 수
# 1231일경우에만 포장 가능.
def solution(ingredient):
    string = ''
    count = 0
    for item in ingredient:
        string += str(item)
        if '1231' == string[-4:]:
            count += 1
            string = string[:-4]
    return count