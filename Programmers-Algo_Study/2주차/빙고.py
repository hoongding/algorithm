# board : N*N 크기의 2차원 배열.
# nums : 지울 숫자가 들어있는 배열.
from collections import deque


def solution(board, nums):
    answer = 0
    len_board = len(board)
    nums = set(nums)  # set은 해시함수.

    for x in range(len_board):
        for y in range(len_board):
            if board[x][y] in nums:
                board[x][y] = 0

    for row in board:  # row 탐색
        if sum(row) == 0:
            answer += 1

    for column in zip(*board):  # column 탐색
        if sum(column) == 0:
            answer += 1

    temp1 = 0
    for i in range(len(board)):  # 대각선 1 탐색
        temp1 += board[i][i]
    if temp1 == 0:
        answer += 1

    temp2 = 0
    for j in range(len(board)):  # 대각선 2 탐색
        temp2 += board[len_board - j - 1][j]
    if temp2 == 0:
        answer += 1

    return answer