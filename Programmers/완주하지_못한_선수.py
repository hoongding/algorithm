# Hash
def solution(participant, completion):
    # participant : 마라톤에 참여한 선수들의 이름이 담긴 배열
    # completion : 완주한 선수들의 이름이 담긴 배열
    # 완주하지 못한 선수의 이름.
    hashDict = {}
    sumHash = 0

    for item in participant:
        hashDict[hash(item)] = item  # 각 아이템을 hashDict에 넣는다.
        sumHash += hash(item)

    for item in completion:
        sumHash -= hash(item)

    print(hashDict[sumHash])

    return hashDict[sumHash]