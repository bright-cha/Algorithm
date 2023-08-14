import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    # 입력문
    code = list(input().split())
    # 빈 스택 생성
    stack = []
    # 인덱스 확인을 위한 top
    top = -1
    for i in code:
        # 숫자 혹은 . 의 경우
        if i not in '+-*/':
            # 숫자의 경우 정수로 바꾸고 스택에 추가한다.
            if i != '.':
                i = int(i)
                stack.append(i)
                top += 1
            # 마침표의 경우 결과값을 출력하고 중지한다.
            else:
                # 남은 스택의 수가 0이라면 출력하고 아니라면 잘못된 식이기에 에러를 출력
                if top == 0:
                    print(f'#{tc}', *stack)
                else:
                    print(f'#{tc}', 'error')
                break


        # 연산기호의 경우
        else:
            # 숫자 2개를 스택에서 pop한다.
            try:
                a2 = stack.pop()
                a1 = stack.pop()
            # 인덱스 에러가 발생하는 경우 식이 성립되지 않기에 에러를 출력하고 중지한다.
            except IndexError:
                print(f'#{tc}', 'error')
                break
            top -= 2

            # 각 기호에 맞게 계산하고 스택에 추가한다.
            if i == '+':
                top += 1
                stack.append(a1 + a2)
            elif i == '-':
                top += 1
                stack.append(a1 - a2)
            elif i == '*':
                top += 1
                stack.append(a1 * a2)
            elif i == '/':
                top += 1
                stack.append(a1 // a2)
