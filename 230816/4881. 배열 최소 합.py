# import sys
# sys.stdin = open('input.txt')
# ##################################


def backtracking(now, size, sum_v):
    global min_v
    # 가지치기
    if min_v < sum_v:
        return

    # 부분집합 완성
    if now == size:
        if min_v > sum_v:
            min_v = sum_v
            return

    # 미완성
    else:
        now += 1
        backtracking(now, size, sum_v)


# T = int(input())
# for tc in range(1, T + 1):
    size = int(input())
    # arr = [list(map(int, input().split())) for _ in range(size)]
    arr = [1, 2, 3, 4, 5]
    min_v = 1e9

    # for i in range(size):
    bit = [0] * size
    # visit = [0] * size
    backtracking(0, size, 0)

    # print(f'#{tc}', min_v)

