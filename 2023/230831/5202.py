def check(idx, leng):
    global max_cnt
    # 신청 목록 1부터 끝까지 체크
    for i in range(apply):
        # i의 사용 기록이 없다면
        if used[i] == 0:
            # 다음 작업 시작시간 선언
            start = start_end[i][0]

            # 만약 이미 사용중인 시간대의 종료시간 <= 다음 작업 시작시간 이라면
            if lst and lst[-1][1] <= start:
                # 대기열 추가
                lst.append(start_end[i])
                # 사용 등록 - 함수 호출 - 사용 초기화
                used[i] = 1
                check(idx + 1, leng)
                used[i] = 0
            # 작업중인 곳이 없다면 언제든 사용가능하므로 추가
            elif not lst:
                lst.append(start_end[i])
                used[i] = 1
                check(idx + 1, leng)
                used[i] = 0

    # 모든 신청목록이 불가하다면 혹은 확인했다면
    # 갯수를 세고 최대값 비교
    cnt = len(lst)
    if max_cnt < cnt:
        max_cnt = cnt
    return


T = int(input())
for tc in range(1, T + 1):
    apply = int(input())
    start_end = [list(map(int, input().split())) for _ in range(apply)]
    # 종료 시간을 기준으로 오름차순 정렬
    start_end.sort(key=lambda x: x[1])
    # 사용 인덱스 체크
    used = [0] * apply
    # 최대값 초기화
    max_cnt = 0
    # 시간대 체크
    lst= []
    # 함수 호출
    check(0, apply)
    print(f'#{tc}', max_cnt)