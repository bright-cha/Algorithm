def binary_search(length, key):  # 이진탐색 함수
    start = 1  # 책의 첫 페이지는 무조건 1
    end = length  # 책의 마지막 페이지

    cnt = 0  # 찾는 횟수
    while True:  # 찾는 페이지는 무조건 있으니 무한 트루
        middle = (start + end) // 2
        if middle == key:
            return cnt
        elif middle < key:
            start = middle  # 문제에 따라 현재의 기준점이 시작점이 된다.
        else:
            end = middle  # 문제에 따라 현재의 기준점이 종료점이 된다.
        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    page, Pa, Pb = map(int, input().split())

    a = binary_search(page, Pa)
    b = binary_search(page, Pb)

    if a > b:  # 찾은 횟수가 a가 많다면 b가 승리
        print(f'#{tc} B')
    elif a < b:  # 찾은 횟수가 b가 많다면 a가 승리
        print(f'#{tc} A')
    else:  # 같다면 0 출력
        print(f'#{tc} 0')