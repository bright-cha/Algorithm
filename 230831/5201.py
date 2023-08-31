T = int(input())
for tc in range(1, T + 1):
    cnt_box, cnt_car = map(int, input().split())
    weight_box = list(map(int, input().split()))
    weight_car = list(map(int, input().split()))
    # 운반할 박스
    rst = []
    # 내림차순 정렬
    weight_car.sort(reverse=True)
    weight_box.sort(reverse=True)

    # 차와 박스 무게를 비교하며 가능할경우 박스를 운반리스트에 넣는다.
    for i in weight_car:
        for j in weight_box:
            if i >= j:
                weight_box.remove(j)
                rst.append(j)
                break

    # 모든 무게를 더해서 출력
    print(f'#{tc}', sum(rst))

