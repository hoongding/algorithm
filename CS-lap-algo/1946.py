# 1946 신입사원 문제
import sys
test_case = int(sys.stdin.readline())
available_people = []
result_list = []


# def find_pass_person(first_ranking, second_ranking):
#     first_max_ranking = min(first_ranking)
#     first_max_index = first_ranking.index(first_max_ranking)  # 첫번째 점수 제일 높은놈의 index
#     first_max_second = second_ranking[first_max_index]  # 첫번재 점수 제일 높은놈의 두번째 점수
#     length = len(first_ranking)
#     pop_index = []
#     for j in range(0, length):  # 조건 안되는 놈 pop.
#         if first_max_second < second_ranking[j]:
#             pop_index.append(j)
#     available_people.append(first_max_index)
#     k = 0
#     for index in pop_index:
#         first_ranking.pop(index - k)
#         second_ranking.pop(index - k)
#         k += 1
#
#     first_ranking.remove(first_max_ranking)
#     second_ranking.remove(first_max_second)


for i in range(0, test_case):
    test_num = int(sys.stdin.readline())
    result = []
    people = []
    count = 1
    for num in range(0, test_num):
        num1, num2 = map(int, sys.stdin.readline().split())
        people.append([num1, num2])
    people.sort()
    max_num2 = people[0][1]

    for j in range(1, test_num):
        if max_num2 > people[j][1] :
            count += 1
            max_num2 = people[j][1]

    print(count)