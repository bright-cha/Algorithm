T = int(input())
for tc in range(1, T+1):
    interval, a_sp, b_sp, bug_sp = map(int, input().split())
    # 파리는 멈추지 않고 날아가기에 A와 B기차가 충돌하기까지
    # 날아가는 거리를 구하면된다.
    # 거리는 시간 X 속력이기에
    # 기차 간 거리를 기차들의 시속으로 나누어 구한다.
    bug_distance = bug_sp * (interval / (a_sp+b_sp))
    print(f'#{tc} {bug_distance}')