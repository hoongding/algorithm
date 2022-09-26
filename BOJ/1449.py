hole_num, tape_len = map(int, input().split())

cur_len = 0
cnt = 0
holes = list(map(int, input().split()))


holes.sort()
for i in range(len(holes)):
    if cur_len <= holes[i] + 0.5: # 지금까지 덮은 공간이
        cur_len = holes[i] - 0.5 + tape_len
        cnt += 1


print(cnt)
