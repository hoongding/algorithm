# 예제 4-1 상하좌우

import sys

map_size = int(sys.stdin.readline())
move_dir = list(map(str, sys.stdin.readline().split()))
start_x = 1
start_y = 1

for direction in move_dir:
    if direction == 'L':
        start_y -= 1
    elif direction == 'R':
        start_y += 1
    elif direction == 'U':
        start_x -= 1
    else:
        start_x += 1
    if start_x < 1:
        start_x += 1
    if start_y < 1:
        start_y += 1
    if start_x > map_size:
        start_x -= 1
    if start_y > map_size:
        start_y -= 1

print(start_x, start_y)
