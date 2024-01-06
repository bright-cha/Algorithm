import sys
from md import *
sys.stdin = open('input.txt')
###############################################
T = int(input())
for tc in range(1, T + 1):
    word = list(input())
    # 스택이 아닌 풀이과정
    # while True:
    #     delete = []
    #     for i in range(len_(word)-1):
    #         if word[i] == word[i + 1]:
    #             delete.append(i)
    #             break
    #     if len_(delete) == 0:
    #         break
    #
    #     for i in delete:
    #         word.remove(word[i])
    #         word.remove(word[i])
    #
    # print(f'#{tc}', len_(word))

    # 스택 빈 리스트 만들기
    stack = []
    for i in word:
        # 스택에 하나씩 넣는다
        stack += i
        # 스택의 길이가 2이상이고 맨 뒤 두개가 같다면
        if len_(stack) > 1 and stack[-1] == stack[-2]:
            # 맨 뒤 두개를 삭제한다.
            stack.pop()
            stack.pop()

    print(f'#{tc}', len_(stack))