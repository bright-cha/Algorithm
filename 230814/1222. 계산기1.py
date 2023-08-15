import sys
sys.stdin = open('input.txt')
########################################################
for tc in range(1, 11):
    leng = int(input())
    code = input()
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    stack = [0] * leng
    # 빈 수식 생성
    math = ''
    top = -1
    for i in code:
        # 피연산자일 경우
        if i != '+':
            # 수식에 저장한다.
            math += i

        # 연산자의 경우
        else:
            # top이 -1이보다 크고 i 보다 top의 우선순위가 크거나 같다면 pop을 해준다.
            # top이 -1이거나 i의 우선순위가 높아지면 while은 무시되고 pop을 진행한다.
            while top > -1 and isp[stack[top]] >= icp[i]:
                math += stack[top]
                top -= 1
            top += 1
            stack[top] = i
    # 스택의 마지막 연산자는 수식에 담기지 않았기에 담아주고 top을 초기화한다.
    math += stack[top]
    top -= 1

    for i in math:
        # 피연사자인 경우
        if i != '+':
            top += 1
            stack[top] = int(i)

        # 연산자인 경우
        else:
            a2 = stack[top]
            top -= 1
            a1 = stack[top]
            top -= 1
            if i == '+':
                top += 1
                stack[top] = a1 + a2
    print(math)

    print(f'#{tc}', stack[top])