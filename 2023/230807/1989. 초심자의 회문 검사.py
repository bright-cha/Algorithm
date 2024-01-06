import sys
sys.stdin = open("input.txt", "r")
#########################################
T = int(input())
for tc in range(1, T+1):
    word = input()
    word_lst = ''.join(list(reversed(word)))
    if word == word_lst:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)

