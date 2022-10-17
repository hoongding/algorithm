# 해시 문제... but set으로 풀어버림
def solution(nums):
    #  N마리 폰켓몬의 종류 번호가 담긴 배열 nums
    #  N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아,
    #  그때의 폰켓몬 종류 번호의 개수를 return
    answer = 0
    set_nums = set(nums)
    if len(set_nums) > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(set_nums)

    return answer