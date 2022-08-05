# 2417번 정수제곱근
import sys

N = int(sys.stdin.readline())


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == N:  # 같으면 바로 mid return
            return mid
        elif mid * mid > N:  # 크면 end = mid - 1로  바꾸기.
            if (mid - 1) * (mid - 1) < N:  # 만약 바로 전 수의 제곱이 N보다 작으면 그놈이 제일 작은 정수임!
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    return


print(binary_search(0, N))
