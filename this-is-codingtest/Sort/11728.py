# 11728번 배열 합치기

N, M = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array = array1 + array2
array.sort()
for i in range(len(array)):
    print(array[i], end=" ")