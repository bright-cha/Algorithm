import sys
sys.stdin = open("input.txt", "r")
#########################################
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    # 결과를 담을 딕셔너리 생성
    rst = {}
    # M의 길이를 가진 문자열들을 추출하기 위해
    # 빈 문자인 word 생성
    for i in range(N):
        for j in range(N-M+1):
            word = ''
            # word에 문자를 길이만큼 추가한다.
            for k in range(j, j+M):
                word += matrix[i][k]
            # 추가된 문자들 즉, 문자열을 rst 딕셔너리에 없다면 0의 값을 가지도록
            # 추가하고 1을 더한다.
            rst.setdefault(word, 0)
            rst[word] += 1
            # 위에서 추가한 문자열을 거꾸로 돌려 없다면 0의 값을 가진 키로 추가하고
            # 1을 더한다. 만약 위에서 추가한 정순과 동일한 문자열일 경우 1+1로 2가된다.
            word = ''.join(list(reversed(word)))
            rst.setdefault(word, 0)
            rst[word] += 1

            # 행렬을 바꾸어 열순회로 위와 동일한 과정을 진행한다.
            word = ''
            for k in range(j, j+M):
                word += matrix[k][i]
            rst.setdefault(word, 0)
            rst[word] += 1
            word = ''.join(list(reversed(word)))
            rst.setdefault(word, 0)
            rst[word] += 1

    # 값이 2인 키를 출력하고 마친다.
    for key, value in rst.items():
        if value == 2:
            print(f'#{tc}', key)
            break





