import sys
sys.stdin = open('bj9663.txt')
##########################################
def check_diag(i, j, size):
    for di, dj in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        ni, nj = i + di, j + dj
        while 0 <= ni < size and 0 <= nj < size:
            if (ni, nj) in local:
                return False
            ni, nj = ni + di, nj + dj

    return True


def check_candidates(size, candidates):
    cnt_candidates = 0
    for i in range(size):
        if used_col[i] == 0:
            candidates[cnt_candidates] = i
            cnt_candidates += 1

    return cnt_candidates


def possible_nqeen(row, size):
    global cnt
    candidates = [0] * size
    # if row == size:
    #     cnt += 1
    #     return

    # else:
    cnt_candidates = check_candidates(size, candidates)
    for i in range(cnt_candidates):
        new_col = candidates[i]
        board[row][new_col] = 1
        used_col[new_col] = 1
        local.append((row, new_col))
        if check_diag(row, new_col, size):
            if row + 1 == size:
                cnt += 1
            else:
                possible_nqeen(row + 1, size)
        board[row][new_col] = 0
        used_col[new_col] = 0
        local.remove((row, new_col))


size = int(input())
board = [[0] * size for _ in range(size)]
used_col = [0] * size
local = []
cnt = 0

possible_nqeen(0, size)

print(cnt)

'''# GPT 풀이
def check_diag(row, col, size, diag_1, diag_2):
    # 대각선 가지치기 함수
    # row와 col을 이용하여 양 대각선에 대한 정보를 확인
    if diag_1[row + col] or diag_2[row - col + size - 1]:
        return False
    return True


def check_candidates(row, size, candidates, used_cols):
    # 열 가지치기 후보 생성 함수
    cnt_candidates = 0
    for col in range(size):
        if not used_cols[col]:
            candidates[cnt_candidates] = col
            cnt_candidates += 1
    return cnt_candidates


def possible_nqeen(row, size, used_cols, diag_1, diag_2):
    global cnt
    candidates = [0] * size
    if row == size:
        cnt += 1
        return

    cnt_candidates = check_candidates(row, size, candidates, used_cols)
    for i in range(cnt_candidates):
        col = candidates[i]
        if check_diag(row, col, size, diag_1, diag_2):
            # 현재 위치가 가능하면 퀸을 배치하고 다음 행으로 이동
            used_cols[col] = True
            diag_1[row + col] = True
            diag_2[row - col + size - 1] = True
            possible_nqeen(row + 1, size, used_cols, diag_1, diag_2)
            # 퀸을 다시 제거하여 백트래킹
            used_cols[col] = False
            diag_1[row + col] = False
            diag_2[row - col + size - 1] = False


size = int(input())
used_cols = [False] * size  # 열 가지치기를 위한 리스트
diag_1 = [False] * (2 * size - 1)  # 대각선 가지치기를 위한 리스트
diag_2 = [False] * (2 * size - 1)  # 대각선 가지치기를 위한 리스트
cnt = 0  # 해의 개수를 저장할 변수

possible_nqeen(0, size, used_cols, diag_1, diag_2)  # 퀸 문제 해결 함수 호출
print(cnt)  # 해의 개수 출력
'''# GPT 풀이