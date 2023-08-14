'''
6525-*2/+
'''

stack = [0] * 100
top = -1
susik = '6525-*2/+'
for x in susik:
    if x not in '+-/*':  # 피연산자면...
        top += 1         # push(x)
        stack[top] = int(x)
    else:
        if x == '+':
        op1 = stack#pop()
        elif x == '-':

        elif x == '/':

        elif x == '*':
