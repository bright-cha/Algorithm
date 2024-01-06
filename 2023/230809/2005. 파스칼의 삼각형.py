import sys
from md import *
sys.stdin = open('input.txt')
###############################################
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N크기 만큼 빈 리스트 생성
    stack = [[] for _ in range(N)]
    
    # N줄을 만들기 위해 반복문 선언
    for i in range(N):
        # 줄에 해당하는 숫자를 선언하기 위해
        # 숫자의 수만큼 반복
        for j in range(i + 1):
            # 각 리스트의 양 옆은 1로 설정
            if j == 0 or j == i:
                stack[i] += [1]
            # 그 외의 경우 이전 행의 2열의 값을 더한다.
            else:
                stack[i] += [stack[i-1][j-1] + stack[i-1][j]]

    print(f'#{tc}')
    for i in range(N):
        print(*stack[i])