import sys
sys.stdin = open('input.txt')
######################################3
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    rst = []

    # 가운데부터 시계방향으로 더해주는 델타를 이용하기 위한 리스트 생성
    di = [0, 0, 0, 1, -1]
    dj = [0, 1, -1, 0, 0]
    for i in range(N):
        for j in range(M):
            # 꽃가루를 더하고 결과값에 저장
            sum_flower = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_flower += matrix[ni][nj]
            rst.append(sum_flower)

    # 최대값 출력
    print(f'#{tc}', max(rst))
