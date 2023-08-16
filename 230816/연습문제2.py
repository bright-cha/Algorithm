# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오.
"""
def subset(i, N, s):  # s는 부분집합의 합
    if i == N:
        if s == 10:
            print(bit)
    else:  # 비트표시를 1과 0 즉, True와 False로 나누어 해당 인덱스에 있는 값이
           # 포함된 부분집합인지 아닌지를 두개로 나누어 살펴본다
        # 비트 표시가 1인경우 True로 포함된 값이기에 s에 해당 값을 더해준다.
        bit[i] = 1
        subset(i + 1, 10, s + lst[i])
        # 비트 표시가 0인경우 False로 포함되지 않은 값이기에 s를 유지한다.
        bit[i] = 0
        subset(i + 1, 10, s)


lst = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * 10
subset(0, 10, 0)
"""
# 강사님 풀이
def solution(arr, k, cnt):
    if cnt != 10:
        return
    for i in range(1, k+1):
        if arr[i] == 1:
            print(data[i], end=' ')
    print()


def make_candidates(arr, k, n, c):
    c[0] = 1  # 선택함
    c[1] = 0  # 선택안함
    return 2  # 생각할 수 있는 경우의 수


def backtracking(arr, k, n, cnt):
    if cnt > 10:  # 유망하지 않으면 가지치기
        return

    c = [0] * 2  # 포함 불포함을 위한 리스트 생성

    if k == n:
        solution(arr, k, cnt)
    else:
        k += 1
        ncandidates = make_candidates(arr, k, n, c)
        for i in range(ncandidates):
            arr[k] = c[i]
            if arr[k] == 1:  # k번째 원소를 선택한 경우
                # 총 합계에 k번째 원소의 값이 더해짐
                backtracking(arr, k, n, cnt + data[k])
            else:
                backtracking(arr, k, n, cnt)
                

MAXCANDIDATES = 12
NMAX = 12

cnt = 0
data = list(range(11))
arr = [0] * NMAX # 각 원소를 사용할 것인지 체크
backtracking(arr, 0, 10, 0)
'''
# 강사님 풀이2
def powerset(arr, k, rst):
    if sum(rst) > 10:
        return

    if k == len(arr):
        if sum(rst) == 10:
            print(rst)
        return

    powerset(arr, k + 1, rst + [arr[k]])
    powerset(arr, k + 1, rst)


arr = list(range(1, 11))

# 원본 배열, 사용한 원소 수, 사용할 원소를 담을 배열
powerset(arr, 0, [])
'''
