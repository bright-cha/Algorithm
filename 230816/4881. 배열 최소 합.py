# import sys
# sys.stdin = open('input.txt')
# ##################################


def backtracking(now, size, sum_v):
    global min_v
    # 가지치기
    if min_v < sum_v:
        return
    unuser_n = [0] * nmax

    # 부분집합 완성
    if now == size:
        if min_v > sum_v:
            min_v = sum_v
            return

    # 미완성
    else:
        now += 1
        ncondidates = ?????????????(now, size, sum_v, unuser_n)
        for i in range(ncondidates):
            backtracking(now, size, sum_v)


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]
    min_v = 1e9
    nmax = size
    bit = [0] * size
    maxcondidates = size + 1

    backtracking(0, size, 0)
