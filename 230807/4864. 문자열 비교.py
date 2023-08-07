import sys
sys.stdin = open("input.txt", "r")
#########################################
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str2를 str1을 기준으로 나눈다.
    str2_rst = str2.split(str1)
    # 나누어진 str2를 문자열로 바꾼다.
    str2_rst = ''.join(str2_rst)

    # 만약 str2와 나누어진 str2가 같지 않다면, str1이 제외된 상태
    # 즉 str1을 가지고 있던 상태였기에 1을출력하고
    # 같다면 str1을 가지고 있지 않았단 것이기에 0을 출력한다.
    if str2 != str2_rst:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)