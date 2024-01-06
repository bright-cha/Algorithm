import sys
from md import *
sys.stdin = open('input.txt')
###############################################
T = 10
for tc in range(1, T + 1):
    length, word = input().split()

    stack = []
    for i in word:
        # 스택에 하나씩 넣는다
        stack += i
        # 스택의 길이가 2이상이고 맨 뒤 두개가 같다면
        if len_(stack) > 1 and stack[-1] == stack[-2]:
            # 맨 뒤 두개를 삭제한다.
            stack.pop()
            stack.pop()

    print(f'#{tc}', ''.join(stack))