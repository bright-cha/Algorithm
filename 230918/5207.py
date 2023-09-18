import sys
sys.stdin = open('input.txt')


def binary_search(start, end, target, direction):
    mid = (start + end) // 2
    # 표적을 찾으면 리턴 트루
    if A[mid] == target:
        return True

    # 표적이 미드보다 큰 경우
    if target > A[mid]:
        # 기록된 방향이 동일하면 폴스 리턴
        if direction == 'right':
            return False
        return binary_search(mid + 1, end, target, 'right')
    # 표적이 미드보다 작은 경우
    else:
        # 기록된 방향이 동일하면 폴스 리턴
        if direction == 'left':
            return False
        return binary_search(start, mid - 1, target, 'left')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for target in B:
        # 타겟 번호가 A안에 있는 경우
        if target in A:
            # 조건을 만족하면 +1
            if binary_search(0, N - 1, target, ''):  # 시작, 마지막 인덱스, 타겟
                cnt += 1

    print(f'#{tc}', cnt)
