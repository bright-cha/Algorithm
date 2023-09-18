import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)

def hoare(left, right):
    # 처음 위치 피봇 설정
    pivot = nums[left]
    # left 위치 조정
    left += 1
    # 교차되기 전까지 반복
    while left <= right:
        # left가 pivot보다 큰 숫자를 찾을 때까지 오른쪽으로 이동
        while left <= right and nums[left] <= pivot:
            left += 1
        # right가 pivot보다 작은 숫자를 찾을 때까지 왼쪽으로 이동
        while left <= right and nums[right] >= pivot:
            right -= 1

        # 교차되지 않았다면 교환
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    # 교차되어 반복문을 빠져나왔기 때문에 right 반환
    return right


def quickSort(left, right):
    # 왼쪽이 오른쪽 보다 크거나 같아지면 = 교차된다면 정렬 완료
    if left >= right:
        return

    # 피봇 탐색 함수 - 호어 파티션
    pivot = hoare(left, right)
    # 맨 처음 위치와 피봇 위치 변경
    nums[left], nums[pivot] = nums[pivot], nums[left]
    # 피봇을 기준으로 왼쪽과 오른쪽 퀵소트 실행행
    quickSort(left, pivot - 1)
    quickSort(pivot + 1, right)


T = int(input())
for tc in range(1, T + 1):
    # 길이
    length = int(input())
    # 숫자들 리스트
    nums = list(map(int, input().split()))
    # 퀵소트
    quickSort(0, length - 1)

    print(f'#{tc}', nums[length // 2])

