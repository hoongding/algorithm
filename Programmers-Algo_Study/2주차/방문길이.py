def solution(dirs):
    coor = [0, 0]
    set_coor = []

    for dir in dirs:
        before_coor = str(coor)
        if dir == 'U':  # y좌표 +1
            coor[1] += 1
            if coor[1] > 5:
                coor[1] = 5
                continue
        elif dir == 'D':  # y좌표 -1
            coor[1] -= 1
            if coor[1] < -5:
                coor[1] = -5
                continue
        elif dir == 'R':  # x좌표 +1
            coor[0] += 1
            if coor[0] > 5:
                coor[0] = 5
                continue
        else:  # x좌표 -1
            coor[0] -= 1
            if coor[0] < -5:
                coor[0] = -5
                continue

        after_coor = str(coor)
        set_coor.append(before_coor + after_coor)
        set_coor.append(after_coor + before_coor)

    return len(set(set_coor)) // 2
