def solution(s):
    answer = True
    s = s.lower()
    p_count = 0
    y_count = 0
    for item in s:
        if 'p' == item:
            p_count += 1
        if 'y' == item:
            y_count += 1
    if p_count != y_count:
        return False

    return True