def backtracking(idx, len):
    global min_v
    # 마지막까지 확인했다면 구한 수열을 행렬에 대입하여 값을 구하고 최소값과 비교
    if idx == len:
        sum_v = 0
        for i in range(size):
            sum_v += matrix[collect_v1[i]][collect_v1[i + 1]]
        if min_v > sum_v:
            min_v = sum_v
        return

    # 아닌 경우 다음 자리 탐색
    else:
        # 첫 자리는 0 고정 / 1 ~ 마지막까지 탐색
        for i in range(1, len):
            # 사용하지 않았다면 추가
            if candidates1[i] == 0:
                collect_v1[idx] = i
                candidates1[i] = 1
                backtracking(idx + 1, len)
                candidates1[i] = 0


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    # 사용한 숫자인지 판별을 위한 리스트
    candidates1 = [0] * size
    # 최종 최소값
    min_v = 1e9
    # 담을 값을 위한 리스트
    collect_v1 = [0] * (size + 1)
    backtracking(1, size)
    print(f'#{tc}', min_v)
