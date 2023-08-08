import sys

sys.stdin = open("input.txt", "r")
#########################################
T = int(input())
for tc in range(1, T + 1):
    # 입력받은 문자열의 문자를 하나씩 꺼내어 0의 값을 가진
    # 키로 이루어진 딕셔너리를 만든다.
    str1 = dict(map(lambda key: (key, 0), input()))
    str2 = input()

    # 만약 str2 문자열의 문자가 str1 딕셔너리에 있다면 값을
    # 1 증가시킨다.
    for word in str2:
        if str1.get(word, -1) != -1:
            str1[word] += 1
    # 최대값을 구한다.
    max_v = 0
    for value in str1.values():
        if max_v < value:
            max_v = value
    # 최대값과 같다면 해당 키를 출력한다.
    for key, value in str1.items():
        if value == max_v:
            print(f"#{tc}", value)
            break