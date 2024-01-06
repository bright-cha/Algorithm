# 이진 검색 - 반복문 활용
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬되어 있다는 조건이 없다면
# 반드시 정렬 먼저 수행해야 함
arr.sort()


def binarySearch(target):
    low = 0
    high = len(arr) - 1

    # low > high 라면 데이터를 몾찾은 경우
    while low <= high:
        middle = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[middle] == target:
            return middle

        # 2. 가운데 값이 정답보다 작은 경우
        elif target > arr[middle]:
            low = middle + 1

        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = middle - 1

    return '해당 데이터는 없습니다.'


print(f'9 = {binarySearch(9)}')
print(f'4 = {binarySearch(4)}')
print(f'10 = {binarySearch(10)}')
