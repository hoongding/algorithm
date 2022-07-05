# 10815번 숫자 카드

card_num = int(input())
card_list = list(map(int, input().split()))
check_card_num = int(input())
check_card_list = list(map(int, input().split()))
result_list = []
card_list.sort()


def binary_search(target, data):
    start = 0
    end = len(card_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


for check in check_card_list:
    if binary_search(check, card_list):
        result_list.append(1)
    else:
        result_list.append(0)

for i in result_list:
    print(i, end=' ')
