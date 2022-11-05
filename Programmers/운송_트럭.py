# 최대무게 한정
# 상품 순서대로 싣는다.
# 상품 실을 수 없는 트럭 바로 목적지로 출발
# max_weight : 트럭 허용무게
# specs : 스펙을 담은 배열
# names : 운반할 상품의 이름이 순서대로 들어있는 배열.

def solution(max_weight, specs, names):
    temp = 0
    cnt = 1
    hash_dict = {}

    for spec in specs:
        hash_dict[spec[0]] = int(spec[1])

    for name in names:
        temp += hash_dict[name]
        if temp > max_weight:
            cnt += 1
            temp = hash_dict[name]

    return cnt
