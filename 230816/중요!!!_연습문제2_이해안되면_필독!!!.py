# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오.
'''# 내 풀이
def subset(now, len_lst, sum_v):  # 순서대로 몇 번째 인덱스 차례인지, 리스트의 길이, 부분집합의 합
    if now == len_lst:    # 모든 차례를 마쳤을 때, 즉 리스트의 길이와 같아졌을 때
        if sum_v == 10:     # 부분집합의 합이 10이라면 포함여부 확인리스트를 이용하여 포함됨이 확인된다면
            for i in range(0, len_lst):    # 해당 값을 출력한다.
                if bit[i] == 1:
                    print(lst[i], end=' ')
            print()

    elif sum_v > 10:         # 가지치기: 부분집합의 합이 10을 넘은 경우 해가 아니기에 넘어간다.
        return

    else:
        # 비트표시를 1과 0 즉, True와 False로 나누어 해당 인덱스에 있는 값이
        # 포함된 부분집합인지 아닌지를 두개로 나누어 살펴본다
        # 비트 표시가 1인경우 True로 포함된 값이기에 sum_v에 해당 값을 더해준다.
        bit[now] = 1
        subset(now + 1, 10, sum_v + lst[now])
        # 비트 표시가 0인경우 False로 포함되지 않은 값이기에 sum_v를 유지한다.
        bit[now] = 0
        subset(now + 1, 10, sum_v)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * len(lst)
subset(0, len(lst), 0)
'''  # 내 풀이
'''
# 강사님 풀이1
# 마지막 조건을 확인하는 솔루션 함수
def solution(bit, now, sum_v):
    # 부분집합 원소의 합이 10이 아니라면 답이 아니기에 None 값 리턴
    if sum_v != 10:
        return
    # 리턴 되지 않음 = 합의 값이 10으로 조건을 충족하였기에,
    # 1부터 마지막자리까지 반복하고,
    for i in range(1, now+1):
        # 만약 해당 자리의 숫자가 포함되었다면 해당 자리의 숫자를 출력한다.
        if bit[i] == 1:
            print(data[i], end=' ')
    print()


def make_candidates(check):
    check[0] = 1  # 선택함
    check[1] = 0  # 선택안함
    return 2  # 0 또는 1의 경우의 가지 수


def backtracking(bit, now, len_data, sum_v):
    # 최종결과로 유망하지 않으면 가지치기 진행
    if sum_v > 10:
        return

    # 0과 1을 체크하기 위한 리스트 / 경우의 수는 0 또는 1이기에 길이는 2개의 인덱스
    check = [0] * 2

    # 만약 진행자리가 리스트의 길이와 같다면, 즉 마지막 진행을 완료했다면
    if now == len_data:
        # 마지막 조건 확인을 위한 솔루션 함수 호출 / 조건 확인을 위해, 포함기록지, 현재 자리, 합 값을 제공
        solution(bit, now, sum_v)

    # 진행단계가 부족하다면, else문을 통해 추가로 진행한다.
    else:
        # 다음자리로 +1
        now += 1

        # 해당 자리 숫자가 포함될지 미포함 될지 경우의 수는 2가지이기에 2의 값을 담는다.
        ncandidates = make_candidates(check)

        # ncandidates의 리턴값은 2로 i는 0, 1 순으로 진행하며
        # 해당 자리가 True인 경우와 False의 경우를 한번에 살펴본다.
        for i in range(ncandidates):
            # 현재 자리의 포함 유무를 기록한다. check[0] = 1, check[1] = 0 으로 포함된 경우부터 살펴본다.
            bit[now] = check[i]  # 0 = 포함 1 = 미포함

            # 현재 자리의 숫자가 부분집합에 포함된 경우,
            if bit[now] == 1:
                # 포함된 경우의 백트래킹을 살펴본다. / 포함되었기 때문에 합 값에 해당 자리 값을 더한다.
                backtracking(bit, now, len_data, sum_v + data[now])

            # 포함되어있지 않은 경우,
            else:
                # 미포합 경우의 백트래킹을 살펴본다. / 포함되지 않았기 때문에 합 값의 변화는 없다.
                backtracking(bit, now, len_data, sum_v)


# 부분집합의 합을 구하기 위한 변수
sum_v = 0
# 0 ~ 10까지의 리스트
data = list(range(11))
# 포함 유무를 파악하기 위한 0과 1의 비트 리스트
bit = [0] * len(data)

# 백트래킹 함수 호출 (포함기록지, 진행자리(시작점 0), 종료인덱스(데이터 길이-1), 부분집합의 합)
# 종료인덱스 -1인 이유: 0의 값은 포함되나마나이고 함수에 들어가는 경우 바로 1증가 되어 1부터 10까지
# 함수가 진행되기 때문에, 데이터 길이가 들어가는 경우, 2부터 11을 탐색하게되어 인덱스 에러가 일어난다.
backtracking(bit, 0, len(data) - 1, sum_v)

'''  # 강사님 풀이1

'''
# 강사님 풀이2
def powerset(bit, now, sum_v):
    # 가지치기
    if sum(sum_v) > 10:
        return
    # 모든 단계를 맞쳤다면  # 부분집합 완성
    if now == len(bit):
        # 포함된 원소들의 합이 10이라면 출력
        if sum(sum_v) == 10:
            print(*sum_v)
        return
    # 가지치기도 아니면서 단계를 마치지 못한경우
    # 배열에 포함된 경우와 포함되지 않은 경우의 함수를 진행
    powerset(bit, now + 1, sum_v + [bit[now]])
    powerset(bit, now + 1, sum_v)


bit = list(range(1, 11)) # 1 ~ 10
# 원본 배열, 진행자리 or 진행 단계, 포함된 원소를 담을 배열
powerset(bit, 0, [])
'''  # 강사님 풀이2
