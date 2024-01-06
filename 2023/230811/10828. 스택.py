import sys
input = sys.stdin.readline

T = int(input())
stack = []
for _ in range(T):
    order = input().strip()
    if 'push' in order:
        word, num = order.split()
        num = int(num)
        stack.append(num)
    elif 'top' == order:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif 'size' == order:
        print(len(stack))
    elif 'pop' == order:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'empty' == order:
        if stack:
            print(0)
        else:
            print(1)