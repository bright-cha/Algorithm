T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    baby_gin = 0  # 베이비 진 횟수
    count = [0] * 12  # 카운트 배열 생성
    for i in range(len(arr)):  # 카운트 배열에 갯수 기입
        count[arr[i]] += 1

    i = 0
    while i < 10:  # 베이비 진 확인
        if count[i] >= 3:
            baby_gin += 1
            count[i] -= 3
            continue
        if count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
            baby_gin += 1
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            continue
        i += 1

    if baby_gin == 2:  # 베이비 진일시 반환값
        baby_gin = 1
    else:
        baby_gin = 0
    print(f'#{tc} {baby_gin}')
