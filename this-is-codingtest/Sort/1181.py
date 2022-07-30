# 1181번 단어 정렬
need_sort = []
for i in range(int(input())):
    temp = input()
    need_sort.append(temp)

need_sort = list(set(need_sort))
set_sort = []
for i in range(len(need_sort)):
    set_sort.append([len(need_sort[i]), need_sort[i]])
set_sort.sort()

for i in range(len(set_sort)):
    print(set_sort[i][1])



