T = int(input())
for tc in range(1, T + 1):
    day = int(input())
    day_price = list(map(int, input().split()))
    # 최종 이윤
    benefit = 0

    # 최대가격
    max_price = 0
    # 뒤에서부터 살펴보며 최대가격보다 크면 갱신
    for i in range(day-1, -1, -1):
        if max_price < day_price[i]:
            max_price = day_price[i]
        # 최대가격보다 작다면 팔고 이윤을 증가한다.
        else:
            benefit += max_price - day_price[i]

    print(f'#{tc}', benefit)