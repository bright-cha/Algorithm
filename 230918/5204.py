import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)

'''
deque를 활용한다면 시간초과가 난다.
따라서 lidx, ridx를 통해 순회하지 않고 해당 인덱스에 바로 접근할 수 있도록 하였다.
'''
def merge(left, right):
    global rst1
    # 만약 왼쪽 마지막 숫자가 크다면 +1
    if left[-1] > right[-1]:
        rst1 += 1

    # 리턴할 리스트 초기화
    result = []

    # 각 리스트별 인덱스 초기화
    lidx, ridx = 0, 0

    # 둘다 숫자가 있다면
    while lidx < len(left) and ridx < len(right):
        # 왼쪽 숫자가 더 작거나 같다면,
        if left[lidx] <= right[ridx]:
            result.append(left[lidx])
            lidx += 1
        # 오른쪽이 더 작다면
        else:
            result.append(right[ridx])
            ridx += 1
    # 왼쪽만 숫자가 있다면
    while lidx < len(left):
        result.append(left[lidx])
        lidx += 1
    # 오른쪽만 숫자가 있다면
    while ridx < len(right):
        result.append(right[ridx])
        ridx += 1

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
    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 카운트
    rst1 = 0
    # 정렬한 리스트 다시 담기
    nums = mergeSort(nums)
    print(f'#{tc}', nums[N//2], rst1)
