import sys
sys.stdin = open('input.txt')
###########################################
for tc in range(1, 11):
    leng = int(input())
    code = input()
    icp = {'*': 2, '+': 1}
    isp = {'*': 2, '+': 1}
    stack = [0] * leng
    top = -1
    math_word = ''
    for i in code:
        # 피연산자일 경우
        if i not in '*+':
            math_word += i
        # 연산자일 경우
        else:
            while top > -1 and isp[stack[top]] >= icp[i]:
                math_word += stack[top]
                top -= 1
            top += 1
            stack[top] = i

    while top > -1:
        math_word += stack[top]
        top -= 1

    for i in math_word:
        # 피연산자인 경우
        if i not in '*+':
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
            elif i == '*':
                top += 1
                stack[top] = a1 * a2

    print(f'#{tc}', stack[top])