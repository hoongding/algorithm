input_sound = list(map(int, input().split()))
c_major = [1, 2, 3, 4, 5, 6, 7, 8]
cnt = 0;
bcnt = 0;

for i in range(len(c_major)):
    if input_sound[i] == c_major[i]:
        cnt += 1

if cnt == 0:
    for i in range(len(c_major)):
        if input_sound[len(c_major)-i-1] == c_major[i]:
            bcnt+=1

if cnt == 8:
    print('ascending')
elif bcnt == 8:
    print('descending')
else: print('mixed')

