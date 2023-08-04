T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    # 각 숫자에 해당하는 인덱스 별로 개수를 기록하기 위한 배열 생성
    count = [0] * 10
    for i in range(N):
        count[arr[i]] += 1

    # 숫자가 큰 인덱스부터 0번 인덱스까지 중 최대값을 가진 인덱스가
    # 있다면 해당 인덱스 번호와 값을 출력한다.
    for j in range(9, -1, -1):
        if count[j] == max(count):
            print(f'#{tc} {j} {count[j]}')
            break