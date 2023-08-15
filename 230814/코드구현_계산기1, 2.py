'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
susik = ''
fx = '(6+5*(2-8)/2)'
for x in fx:
    # 피연산자의 경우
    if x not in '(+-*/)':  # 피연산자
        susik += x

    # 닫는 괄호의 경우
    elif x == ')':         # '(' 까지 pop()
        while stack[top] != '(':  # peek
            susik += stack[top]
            top -= 1
        top -= 1                  # '(' 버림. pop

    # 연산자의 경우
    else:    # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
            top += 1       # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1        # push
            stack[top] = x
# 연산자인 경우 아래와 같이 간단하게 사용가능하다. (내가 직접 줄인 것)
'''
    else:
            # top이 -1이보다 크고 i 보다 top의 우선순위가 크거나 같다면 pop을 해준다.
            # top이 -1이거나 i의 우선순위가 높아지면 while은 무시되고 pop을 진행한다.
            while top > -1 and isp[stack[top]] >= icp[i]:
                math += stack[top]
                top -= 1
            top += 1
            stack[top] = i
'''
print(susik)

for x in susik:
    if x not in '+-/*':   # 피연산자면...
        top += 1          # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x == '+':
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
print(stack[top])