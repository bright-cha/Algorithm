def partition(lst, start, end):
    pivot = (start + end) // 2  # 피봇은 중앙인덱스
    L = start
    R = end
    while L < R:  # 시작 지점이 엔드 지점보다 같거나 커지면 종료한다.
        while lst[L] < lst[pivot] and L < R:  # 피봇보다 작다면 하나씩 오른쪽으로
            L += 1                            # 이동하며 큰 값을 찾는다.
        while lst[R] >= lst[pivot] and L < R:  # 피봇보다 크다면 하나씩 왼쪽으로
            R -= 1                             # 이동하며 작은 값을 찾는다.
        if L < R:  # 위의 과정이 끝나도 시작점이 끝점보다 작다는 것은 L 또는 R이 원하는 값을 찾았다는 것
            if L == pivot:  # 피봇보다 큰 값을 찾지 못했다면, R의 자리가 피봇이 된다.
                pivot = R
            lst[L], lst[R] = lst[R], lst[L]  # 왼쪽에 큰값과 오른쪽의 작은값을 교환한다.
    lst[pivot], lst[R] = lst[R], lst[pivot]  # 피봇을 기준으로 양옆에 정렬이 완료 되었으므로 기준값을 큰값으로 바꾼다.
    return R  # 큰 값인 R을 다음 피봇으로 리턴해준다.


def quickSort(lst, start, end):  # 배열, 스타트, 끝
    if start < end:
        p = partition(lst, start, end)  # 파티션 함수를 통해 피봇값을 재설정하고 재귀한다.
        quickSort(lst, start, p - 1)    # 리턴받은 피봇을 기준으로 양쪽으로 퀵소트를 진행한다.
        quickSort(lst, p + 1, end)


arr = [5, 216, 46, 4, 63, 54, 89, 4, 3, 1, 64, 6, 456, 41, 3]
quickSort(arr, 0, len(arr)-1)
print(arr)