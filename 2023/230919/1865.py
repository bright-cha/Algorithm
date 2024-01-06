import sys
sys.stdin = open('input.txt')


def backtracking(idx, probability):
    global max_pro, col

    # 모든 직원별 작업을 지정했다면
    if idx == cnt_employee:
        max_pro = max(max_pro, probability)
        return

    # 아직 남은 작업이 있다면
    else:
        # 모든 작업 횟수 조회
        for i in range(cnt_employee):
            # 아직 배정되지 않은 작업이고, 작업 확률이 0이 아닌 경우 배정
            if col[i] == 0 and works[idx][i] != 0:
                col[i] = 1
                probability *= (works[idx][i] / 100)
                # 가지치기 - 배정된 후 확률이 줄어든다면 넘김
                if probability < max_pro:
                    # 확률 원상복귀
                    probability /= (works[idx][i] / 100)
                    col[i] = 0
                    continue
                backtracking(idx + 1, probability)
                # 확률 원상 복귀
                probability /= (works[idx][i] / 100)
                col[i] = 0


T = int(input())
for tc in range(1, T + 1):
    # 직원 수
    cnt_employee = int(input())
    # 직원별 작업
    works = [list(map(float, input().split())) for _ in range(cnt_employee)]
    # 최종 최대값
    max_pro = 0
    # 방문 표시
    col = [0] * cnt_employee

    backtracking(0, 1.0)
    print(f'#{tc} {max_pro * 100:.6f}')