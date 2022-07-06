# 10816번 숫자카드2
import sys
from collections import Counter
card_num = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
check_card_num = int(sys.stdin.readline())
check_card_list = list(map(int, sys.stdin.readline().split()))
result_list = []
count_card = Counter(card_list)

for check in check_card_list:
    if check in count_card:
        result_list.append(count_card[check])
    else:
        result_list.append(0)
for i in result_list:
    print(i, end=' ')
