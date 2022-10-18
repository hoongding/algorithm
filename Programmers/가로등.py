def find_d(distance):
    if distance % 2 == 0:
        d = distance // 2
    else:
        d = (distance // 2) + 1
    return d


def solution(l, v):
    v.sort()
    d = []
    if v[0] != 0:
        d.append(v[0])

    for i in range(len(v) - 1):
        next_dis = v[i + 1] - v[i]
        d.append(find_d(next_dis))

    if v[-1] != l:
        next_dis = l - v[-1]
        d.append(l - v[-1])

    return max(d)