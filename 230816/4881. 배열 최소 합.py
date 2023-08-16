import sys
sys.stdin = open('input.txt')
##################################


def backtracking()


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]
    bit = [0] * size
    min_v = 1e9

    backtracking(order, last_order)

    print(f'#{tc}', min_v)

