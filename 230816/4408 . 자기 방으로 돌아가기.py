import sys
sys.stdin = open('input.txt')
#######################################
T = int(input())
for tc in range(1, T + 1):
    cnt_std = int(input().strip())
    now_should_room = [list(map(int, input().strip().split())) for _ in range(cnt_std)]
    room_to_room = [0] * 401
    cnt = 1
    for start, end in now_should_room:
        if start > end:
            start, end = end, start
        if end % 2 == 1:
            end += 1
        if start % 2 == 1:
            start += 1
        for j in range(start, end + 1):
            room_to_room[j] += 1  # 복도에 학생 수 추가

    print(f'#{tc}', max(room_to_room))