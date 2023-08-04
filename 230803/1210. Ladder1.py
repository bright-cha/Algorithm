for tc in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 도착점부터 시작하기 위해 숫자 2가 적힌 좌표를 구한다.

    # 행의 값 a / 도착점은 마지막 행이기 때문에 99를 넣는다.
    a = 99
    # 열의 값 b / index 메서드를 통해 2의 값을 가진 인덱스를 찾는다.
    b = matrix[a].index(2)

    # 도착점 옆에 다른 도착점, 즉 1이 있을 수 있기 때문에
    # 한 칸 위에서 시작한다.
    a = 98
    while a:
        # 옆에 길이 있는지 탐색하고 길이 있다면 옆으로 이동한다.
        if b != 99 and matrix[a][b + 1]:
            matrix[a][b] = 0
            b += 1
        elif b and matrix[a][b - 1]:
            matrix[a][b] = 0
            b -= 1
        # 양 옆에 길이 없다면 위로 올라간다.
        else:
            a -= 1

    print(f'#{T}', b)