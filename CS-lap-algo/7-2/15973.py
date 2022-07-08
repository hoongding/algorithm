# 15973번 두 박스
box1_x1, box1_y1, box1_x3, box1_y3 = map(int, input().split())
box2_x1, box2_y1, box2_x3, box2_y3 = map(int, input().split())

box_1 = [[box1_x1, box1_y1], [box1_x3, box1_y1], [box1_x3, box1_y3], [box1_x1, box1_y3]]
box_2 = [[box2_x1, box2_y1], [box2_x3, box2_y1], [box2_x3, box2_y3], [box2_x1, box2_y3]]


def is_point(box1, box2):  # 한점만 겹치면 count 1 // 안겹치면 0
    if box1[0] == box2[2] or box1[2] == box2[0]:
        return True
    if box1[1] == box2[3] or box1[3] == box2[1]:
        return True
    return False


def is_line(box1, box2):
    if box1[0][1] == box2[2][1] or box1[2][1] == box2[0][1]:
        return True
    if box1[1][0] == box2[0][0] or box1[0][0] == box2[1][0]:
        return True

    return False


def is_null(box1, box2):
    if box1[0][1] > box2[2][1] or box1[2][1] < box2[0][1]:
        return True
    if box1[1][0] < box2[0][0] or box1[0][0] > box2[1][0]:
        return True

    return False


if is_null(box_1, box_2):
    print("NULL")
elif is_point(box_1, box_2):
    print("POINT")
elif is_line(box_1, box_2):
    print("LINE")
else:
    print("FACE")
