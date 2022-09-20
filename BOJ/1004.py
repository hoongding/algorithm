def find_distance(x, y, cx, cy, r):
    d = (cx-x)**2 + (cy - y)**2
    if d <= r**2:
        return True
    else:
        return False

test_num = int(input())
for i in range(test_num): # test 개수만큼 반복
    x1, y1, x2, y2 = map(int, input().split())
    start_info = []
    end_info = []
    planet_num = int(input()) # 행성 개수
    count = 0
    for j in range(planet_num):
        cx, cy, r = map(int, input().split())
        if find_distance(x1, y1, cx, cy, r) and find_distance(x2, y2, cx, cy, r):
            pass
        elif find_distance(x1, y1, cx, cy, r):
            count += 1
        elif find_distance(x2, y2, cx, cy, r):
            count += 1

    print(count)
