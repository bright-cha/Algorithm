import sys
sys.stdin = open("input.txt")
###########################################################
T = int(input())
for tc in range(1, T + 1):
    # 인덱스 개수를 줄이기 위해 10으로 나눠줌
    N = int(input()) // 10
    # 길이별로 경우의 수 기록을 위한 인덱스 생성
    tile = [0] * (N + 1)
    tile[1] = 1
    tile[2] = 3
    for i in range(3, N + 1):
        tile[i] = tile[i - 1] + (tile[i - 2] * 2)
    print(f'#{tc}', tile[N])