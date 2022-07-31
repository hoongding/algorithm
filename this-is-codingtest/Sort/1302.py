# 1302번 베스트셀러
from collections import Counter

sell_book = []
for i in range(int(input())):
    sell_book.append(input())

most = Counter(sell_book).most_common()
most.sort(reverse=True)
print(most)
