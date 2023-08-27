import sys
sys.stdin = open('input.txt')
#########################################
T = 10
for tc in range(1, T + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    cnt = 0
    for i in range(size):
        for j in range(size):
            # 만약 1이 있다면
            if matrix[j][i] == 1:
                # 다음 열부터 파악한다 .
                for k in matrix[j+1:size]:
                    # 1이면 멈추고 2이면 실행한다.
                    if k[i] == 1:
                        break
                    elif k[i] == 2:
                        cnt += 1
                        break

    print(f'#{tc}', cnt)