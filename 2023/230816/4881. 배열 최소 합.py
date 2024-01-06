import sys
sys.stdin = open('input.txt')
#######################################
def check_candidates(idx, max_len, candidates):
    used_num = [False] * (max_len + 1)

    for i in range(1, idx):
        used_num[collected[i]] = True

    cnt_candidates = 0
    for i in range(1, max_len + 1):
        if not used_num[i]:
            candidates[cnt_candidates] = i
            cnt_candidates += 1

    return cnt_candidates


<<<<<<< HEAD
def backtrack(idx, max_len):
    global collected
    global min_value
    sum_v = 0
    row = 0
    for i in range(1, idx + 1):
        sum_v += matrix[row][collected[i] - 1]
        row += 1
        if sum_v > min_value:
            return
    candidates = [0] * (max_len + 1)
=======
def backtracking(now, size, sum_v):
    global min_v
    # 가지치기
    if min_v < sum_v:
        return
    unuser_n = [0] * nmax
>>>>>>> 74b3726dd9442f5d683d17f2473ea665f744f43d

    if idx == max_len:
        if sum_v < min_value:
            min_value = sum_v
            return

    else:
<<<<<<< HEAD
        idx += 1
        ncandidates = check_candidates(idx, max_len, candidates)
        for i in range(ncandidates):
            collected[idx] = candidates[i]
            backtrack(idx, max_len)




T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    max_len = size
    collected = [0] * (size + 1)
    min_value = 1e9

    backtrack(0, max_len)
    print(f'#{tc}', min_value)
=======
        now += 1
        ncondidates = ?????????????(now, size, sum_v, unuser_n)
        for i in range(ncondidates):
            backtracking(now, size, sum_v)


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]
    min_v = 1e9
    nmax = size
    bit = [0] * size
    maxcondidates = size + 1

    backtracking(0, size, 0)
>>>>>>> 74b3726dd9442f5d683d17f2473ea665f744f43d
