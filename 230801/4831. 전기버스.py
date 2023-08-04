T = int(input())
for tc in range(1, T + 1):
    # k = 이동가능 n = 목표 m = 충전기 설치 정류장
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    stop = [0] * (N + 1)  # 정류장 개수
    bus = K - 1  # 버스가 가진 연료

    # 충전횟수
    cnt = 0

    # 목표 정류장까지 반복
    for i in range(1, N + 1):
        # 해당 정류장이 충전소인지 확인
        if i in arr:
            # 현재위치에서 다음 충전소 길이를 구하고
            # 길이에 비해 남은 연료가 부족하다면 충전
            if len(arr) == 1 and bus < N - i:
                cnt += 1
                bus = K
            elif len(arr) != 1 and bus < arr[1] - i:
                cnt += 1
                bus = K
            arr.remove(i)
        else:
            # 정류장이 목표가 아니면서 연료가 없다면 반복문 종료
            if i != N and bus == 0:
                cnt = 0
                break
        # 다음 정류장에 도착하기 전 연료 사용
        bus -= 1

    print(f'#{tc} {cnt}')