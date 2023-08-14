import sys
sys.stdin = open('input.txt')
leng = int(input())
code = input()
icp = {'(' : 3, '*':2, '/':2, '+':1, '-' : 1}
isp = {'(' : 0, '*':2, '/':2, '+':1, '-' : 1}
stack = []
top = -1
for i in code:
    # 피연사자인 경우
    if i not in '+-*/':
        top += 1
        stack.append(int(i))

    # 연산자인 경우
    else:
        if top == -1 or icp[i] > isp[i]




        a2 = stack.pop()
        a1 = stack.pop()
        top -= 2
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
            stack.append(a1 / a2)

print(stack)