import sys
sys.stdin = open('input.txt')
########################################
K = int(input())
stack = []
for _ in range(K):
    stack.append(int(input()))
    if not stack[-1]:
        stack.pop()
        stack.pop()

print(sum(stack))