import sys
from md import *
sys.stdin = open('input.txt')
###############################################
T = int(input())
for tc in range(1, T + 1):
    word = input().strip()
    bracket = ['{', '}', '(', ')']

    # 문자가 괄호라면 lst에 담는다.
    lst = []
    for i in word:
        if in_(bracket, i):
            lst.append(i)

    # 스택 초기화
    stack = []
    for i in lst:
        # 스택에 한 글자씩 담는다.
        stack += i

        # 오른쪽 괄호가 들어왔을때 해당 괄호를 지운 후,
        if i == ')':
            stack.pop()
            # 스택이 비었거나, 마지막 문자가 {라면 0 출력 {)     )
            if len_(stack) == 0 or stack[-1] == '{':
                print(f'#{tc} 0')
                break
            # 아니라면 삭제
            else:
                stack.pop()

        # 오른쪽 괄호가 들어왔을때 해당 괄호를 지운 후,
        if i == '}':
            stack.pop()
            # 스택이 비었거나, 마지막 문자가 (라면 0 출력
            if len_(stack) == 0 or stack[-1] == '(':
                print(f'#{tc} 0')
                break
            # 아니라면 삭제
            else:
                stack.pop()

    # 모두 실행됐을 때,
    else:
        # 남은 스택 길이가 0이라면 1출력, 아니라면 0출력
        if len_(stack) == 0:
            print(f'#{tc}', 1)
        else:
            print(f'#{tc}', 0)