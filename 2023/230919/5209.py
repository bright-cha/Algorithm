import sys
sys.stdin = open('input.txt')


def backtracking(idx, total, cost):
    global min_cost, row, col
    # 가지치기
    if cost >= min_cost:
        return

    # 마지막 단계
    if idx == total:
        min_cost = min(min_cost, cost)
        return

    # 마지막 단계가 아닌 경우,
    else:
        # 공장 정하기
        for i in range(cnt_product):
            # 가지치기
            if row[i] == 0:
                row[i] = 1
                # 재귀
                backtracking(idx + 1, total, cost + factory_procost[idx][i])
                # 초기화
                row[i] = 0


T = int(input())
for tc in range(1, T + 1):
    # 제품수
    cnt_product = int(input())
    # 공장_비용
    factory_procost = [list(map(int, input().split())) for _ in range(cnt_product)]

    # 최종 생산 비용
    min_cost = 1e7
    # 기록지
    row = [0] * cnt_product

    backtracking(0, cnt_product, 0)
    print(f'#{tc}', min_cost)