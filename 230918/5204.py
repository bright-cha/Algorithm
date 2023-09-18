import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)

from collections import deque


def merge(left, right):
    global rst1
    # 만약 왼쪽 마지막 숫자가 크다면 +1
    if left[-1] > right[-1]:
        rst1 += 1

    # 리턴할 리스트 초기화
    result = []
    # 가져와야할 숫자가 있다면 반복
    ll = len(left)
    lr = len(right)
    # while ll > 0 or lr > 0:
    # 둘다 숫자가 있다면
    while ll > 0 and lr > 0:
        # 왼쪽 첫 번째 숫자가 더 작거나 같다면,
        if left[0] <= right[0]:
            result.append(left.popleft())
            ll -= 1
        # 오른쪽이 더 작다면
        else:
            result.append(right.popleft())
            lr -= 1
    # 왼쪽만 숫자가 있다면
    while ll:
        result.append(left.popleft())
        ll -= 1
    # 오른쪽만 숫자가 있다면
    while lr:
        result.append(right.popleft())
        lr -= 1

    return result


# 분할단계
def mergeSort(lst):
    # # 길이가 1이라면 리턴
    # if len(lst) == 1:
    #     return lst

    # 길이가 2이상이라면 좌우로 나누기 위한 기준점
    mid = len(lst) // 2
    # 빈 리스트 생성
    left, right = [], []
    # 기준점을 기준으로 담는다.
    for i in lst[0: mid]:
        left.append(i)
    for i in lst[mid: len(lst)]:
        right.append(i)

    # 각 리스트의 길이가 1이 될 때까지, 재귀
    if len(left) > 1:
        left = mergeSort(left)
    if len(right) > 1:
        right = mergeSort(right)

    # 병합단계를 거친 값을 리턴
    return merge(deque(left), deque(right))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 카운트
    rst1 = 0
    # 정렬한 리스트 다시 담기
    nums = mergeSort(nums)
    print(f'#{tc}', nums[N//2], rst1)
