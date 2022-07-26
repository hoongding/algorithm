# 9019 DSLR
from collections import deque
import sys

def do_D(num):
    ret = (num * 2) % 10000
    return ret


def do_S(num):
    if num == 0:
        return 9999
    ret = num - 1
    return ret


def do_L(num):
    a = num % 1000
    b = num // 1000
    ret = a * 10 + b
    return ret


def do_R(num):
    a = num % 10
    b = num // 10
    ret = a*1000 + b
    return ret


def bfs(num1, num2):
    q = deque()
    visited = [False]*10000  # 이미 방문한 놈인지 아닌지
    q.append((num1, ""))
    visited[num1] = True
    while q:
        a, b = q.popleft()
        if a == num2:
            print(b)
            return
        temp = do_D(a)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, b + "D"))

        temp = do_S(a)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, b + "S"))

        temp = do_L(a)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, b + "L"))

        temp = do_R(a)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, b + "R"))


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    num1, num2 = map(int, sys.stdin.readline().split())
    bfs(num1, num2)
