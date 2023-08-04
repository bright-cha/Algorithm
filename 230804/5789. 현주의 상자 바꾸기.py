T = int(input())
for tc in range(1, T + 1):
    # 박스 갯수와 작업 횟수
    box_nums, cnt = map(int, input().split())
    # 박스마다 0을 담는다.
    box = [0] * box_nums

    # 작업횟수만큼 반복한다. 박스는 1번부터 시작이니
    # i도 1번부터 시작할 수 있게 만든다.
    for i in range(1, cnt + 1):
        L, R = map(int, input().split())
        # 또한, 배열은 0번 인덱스부터 시작하고,
        # L, R이 1, 3 인 경우 / 1,2,3 에 숫자를 넣어야하기에
        # L-1부터 R-1번 영역을 R-L+1개의 i를 담은 리스트로 바꿔준다.
        box[L - 1:R] = [i] * (R - L + 1)

    print(f'#{tc}', *box)