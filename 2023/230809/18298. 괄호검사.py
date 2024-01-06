import sys
# sys.stdin = open('input.txt')
###############################################
T = int(input())
for tc in range(1, T + 1):
    word = input().strip()

    # 스택을 위한 리스트
    rst = []
    for i in word:
        rst += i
        # 한 글자씩 넣고, 0번 인덱스가 (인 상태로 )가 들어온다면 TOP을 2개 삭제한다.
        if rst[0] == '(' and ')' in rst:
            rst.pop()
            rst.pop()

    # 만약 리스트가 비어있다면 1 아니라면 -1을 출력한다.
    if len(rst) == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', -1)
