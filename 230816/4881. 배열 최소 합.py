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

    if idx == max_len:
        if sum_v < min_value:
            min_value = sum_v
            return

    else:
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