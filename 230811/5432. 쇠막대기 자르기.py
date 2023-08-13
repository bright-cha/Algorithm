import sys
sys.stdin = open('input.txt')
##################################
T = int(input())
for tc in range(1, T + 1):
    stack = list(map(str, input().strip()))

    # 최종 조각난 막대기
    cnt = 0
    # 전체 레이저 갯수
    laser = 0
    # 막대기에 닿지 않는 레이저
    side_laser = []
    # 전체 막대기 개수
    stick = 0
    # 짧은 막대기 = 닿지 않는 레이저가 있는 막대기 개수
    short = 0
    while stack:
        # 닫는 괄호일 경우 삭제
        if stack[-1] == ')':
            stack.pop()
            # Top이 여는 괄호일 경우 레이저, 삭제하고 1개 증가
            if stack[-1] == '(':
                stack.pop()
                laser += 1
                # 막대기가 없다면 레이저는 다시 뺀다.
                if stick == 0:
                    laser -= 1

            # Top이 닫는 괄호인 경우, 막대기, 삭제하고 1 증가
            else:
                stick += 1
                # 막대기가 생기기 전에 있던 레이저는 닿지 않기 때문에, 그 수만큼 side_laser가 되고 짧은 막대기 수 증가.
                if laser != 0:
                    side_laser.append(laser)
                    short += 1

        # 여는 괄호인 경우, 막대기의 시작지점이다.
        else:
            # 막대기 제거
            stack.pop()
            # 만약 사이드레이저가 있다면 s에 저장 없다면 0저장
            if side_laser:
                s = side_laser.pop()
            else:
                s = 0
            # 조각난 횟수 = 전체 레이저 갯수 + 1 에서 닿지 않는 레이저 수 빼기
            cnt += laser + 1 - s
            # 짧은 막대기가 있다면, 제거한 막대기는 짧은 막대기다
            if short > 0:
                # 제거된 짧은 막대기 갯수 감소
                short -= 1
            # 막대기 갯수 1 감소
            stick -= 1
            # 만약 막대기가 없다면 레이저는 사라진다.
            if stick == 0:
                laser = 0

    print(f'#{tc}', cnt)
'''
주어진 테스트 케이스 개수 T
T = int(input())

for tc in range(1, T + 1):

    # 쇠막대기와 레이저의 배치
    stick_razer_pos = input().strip()

    # push와 pop을 할 빈 스택
    stack = 0
    # 최종적으로 구해야하는 잘려진 조각의 개수를 초기값 0으로 세팅
    pieces = 0
    # 전 괄호를 저장할 빈 문자열
    previous = ""

    for char in stick_razer_pos:

        # 만약 왼쪽 괄호라면 push
        if char == "(":
            stack += 1

        # 만약 오른쪽 괄호라면
        else:
            # 전에 있던 괄호가 왼쪽 괄호라면
            if previous == "(":
                stack -= 1  # pop을 하므로 stack은 -1
                pieces += stack  # stack에 있는 개수를 조각에 더함
            # 전에 있던 괄호가 오른쪽 괄호라면
            else:
                stack -= 1  # pop을 하므로 stack은 -1
                pieces += 1  # 마지막 잘린 개수를 1을 pieces에 더한다

        # 방금 확인한 char은 이제 previous로 저장
        previous = char

    # 출력
    print(f"#{tc} {pieces}")
'''