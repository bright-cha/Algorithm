import sys
sys.stdin = open('input.txt')


def backtracking(idx, finish, cnt_charge):
    global min_charge

    # 만약 도착지 도착이라면
    if idx >= finish:
        min_charge = min(min_charge, cnt_charge)
        return

    # 아니라면
    else:
        # 현재에서 충전
        charge = bus_stop[idx]
        # 충전한만큼 갈 수 있는 거리구해서 재귀
        for i in range(1, charge + 1):
            # 최소 충전 수 넘어가면 리턴
            if cnt_charge + 1 >= min_charge:
                return
            backtracking(idx + i, finish, cnt_charge + 1)


T = int(input())
for tc in range(1, T + 1):
    temp = list(map(int, input().split()))
    # 도착지를 제외한 정류장
    bus_stop = temp[1:]
    # 도착지
    end = temp[0] - 1

    # 최종 최소 충전 수
    min_charge = 1e7
    backtracking(0, end, -1)
    print(f'#{tc}', min_charge)