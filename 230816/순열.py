'''# 라이브 풀이
#순열1
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i + 1, N)
            A[i], A[j] = A[j], A[i]


A = [1,2,3]
f(0, 3)

# 출력값
# [1, 2, 3] 0 0 1 1 2 2
# [1, 3, 2] 1 2
# [2, 1, 3] 0 1
# [2, 3, 1] 0 1 1 2
# [3, 2, 1] 0 2
# [3, 1, 2] 0 2 1 2
 # 라이브 풀이
'''
<<<<<<< HEAD


# 교재 풀이
def check_candidates(collected, idx, input, candidates):
    used_num = [False] * (NMAX + 1)  # 사용된 숫자를 체크하기 위한 리스트로, 모두 미사용으로 초기화

    for i in range(1, idx):           # 첫 번째 자리부터 이전 자리까지 살펴본다.
        used_num[collected[i]] = True  # collected[해당 자리] 즉, 사용된 숫자를
                                      # used_num 리스트의 해당 인덱스를 True 사용됨을 표시
=======

'''# 교재 풀이
def construct_candidates(data, idx, max_num, unused_num):
    # 포함된 숫자의 확인을 위해 리스트 생성
    in_perm = [False] * NMAX

    # now가 1인 경우는 아직 아무 숫자도 사용되지 않았기 때문에 사용한 숫자를 찾을 필요가 없음
    for i in range(1, idx):
        in_perm[data[i]] = True
>>>>>>> 74b3726dd9442f5d683d17f2473ea665f744f43d

    cnt_candidates = 0  # 후보의 갯수 0 초기화
    for i in range(1, NMAX + 1):  # 1번 숫자부터 마지막 숫자까지 후보가 될 수 있는지 살펴본다
        if used_num[i] == False:    # 해당 숫자의 인덱스가 False 즉, 미사용 표시라면
            candidates[cnt_candidates] = i  # 후보 리스트 0번 인덱스부터 미사용 숫자를 넣어둔다.
            cnt_candidates += 1             # 다음 미사용 숫자 자리를 확보하고 후보의 갯수 파악을 위해 +1

    return cnt_candidates             # 모든 숫자를 살펴본 후 후보 갯수 즉, 미사용 숫자의 개수만큼 리턴


<<<<<<< HEAD
def backtrack(collected, idx, input):
    global MAXCANDIDATES
    candidates = [0] * MAXCANDIDATES  # 각 자리에 올 수 있는 후보 리스트
    # 마지막 자리까지 확인했다면,
    if idx == input:
        # 1부터 마지막 자리까지 반복하며, 해당 자리 숫자 출력
        for i in range(1, input + 1):
            print(collected[i], end=' ')
=======
def backtrack(data, idx, max_num):
    global MAXCANDIDATES  # MAXCANDIDATES = 3
    # 최고숫자만큼 포함되지 않은 숫자들을 저장할 리스트 생성 / 미포함 리스트
    unused_num = [0] * MAXCANDIDATES

    # 3까지 포함시켰다면, 즉 모든 단계를 진행했다면
    if idx == max_num:
        # 1부터 마지막 숫자까지 반복하며, 포함되는 해당 원소 출력
        for i in range(1, idx + 1):
            print(data[i], end=' ')
>>>>>>> 74b3726dd9442f5d683d17f2473ea665f744f43d
        print()
    # 마지막 자리까지 확인하지 않고 남은 자리가 있다면,
    else:
<<<<<<< HEAD
        # 다음자리확인
        idx += 1
        # 후보를 찾고 그 개수를 리턴받아 변수에 담는다.
        ncandidates = check_candidates(collected, idx, input, candidates)
        for i in range(ncandidates):  # 후보를 적용하기 위해 갯수 만큼 반복
            collected[idx] = candidates[i]  # 현재 확인하는 자리에 후보 즉, 미사용된 숫자를 결과값에 넣고
            backtrack(collected, idx, input) # 남은 뒷자리도 알아보고 결과를 받기 위해 재귀시킨다.


MAXCANDIDATES = 3  # 후보의 최고 길이
NMAX = 3           # 최고 숫자
collected = [0] * (MAXCANDIDATES+1)  # 각 자리별로 숫자를 채우기 위해 초기화
backtrack(collected, 0, MAXCANDIDATES)  # 채워진 숫자, 0 = 1번 자리부터 채우기 위해, 3 = 숫자의 길이 ex) 123

=======
        # 단계 +1
        idx += 1

        # 남은 자리에 추가 가능한 숫자 구하기
        # construct_candidates 함수를 통해 이전 단계에서 사용되지 않은 숫자를 구하고 그 개수를 리턴받는다.
        ncandidates = construct_candidates(data, idx, max_num, unused_num)

        # 포함되지 않은 숫자 개수만큼 반복
        for i in range(ncandidates):
            # 집합의 현재 자리에 미포함 리스트에 저장됐던 숫자 저장
            data[idx] = unused_num[i]
            # 추가된 집합을 적용한 백트래킹 함수 호출
            backtrack(data, idx, max_num)


# 후보가 될 수 있는 자리
MAXCANDIDATES = 3

# 0부터 시작하는 모든자리
NMAX = 4

# 부분집합(수열)을 담을 리스트 생성
data = [0] * NMAX

# 순열, 현재자리 or 현재단계(0부터 시작), 최고숫자를 제공하는 백트래킹 호출
backtrack(data, 0, MAXCANDIDATES)
'''# 교재 풀이
>>>>>>> 74b3726dd9442f5d683d17f2473ea665f744f43d
