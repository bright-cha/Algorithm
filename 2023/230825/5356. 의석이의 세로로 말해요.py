import sys
sys.stdin = open('input.txt')
#################################
# 한 좌표를 기준으로 k영역을 확인하는 함수 / 좌표를 기준으로 찾아갈수 있는 델타리스트를 리턴한다.
def chack_area(K):
    delta_lst = []
    for i in range(-(K-1), K):
        for j in range(-(K - 1), K):
            if abs(i) + abs(j) < K:
                delta_lst.append((i, j))
    return delta_lst


T = int(input())
for tc in range(1, T + 1):
    size, one_cost = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(size)]

    # 모든 집의 개수 확인
    all_cnt = 0
    for i in range(size):
        for j in range(size):
            if city[i][j] == 1:
                all_cnt += 1

    # 서비스 영역
    k = 1
    # 종료조건을 만나면 0으로 변경해서 반복문 종료
    flag = 1
    # 출력을 위한 최대 개수
    max_v = 0
    # 돌때마다 k값 증가
    while flag:
        # 운영 비용 확인
        oper_cost = k ** 2 + (k - 1) ** 2
        # 모든 지역 확인
        for i in range(size):
            for j in range(size):
                # 서비스 지역 내 집의 개수
                cnt_house = 0
                # 서비스 영역 확인 함수를 통해 리턴받은 델타리스트를 활용
                for di, dj in chack_area(k):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < size and 0 <= nj < size:
                        if city[ni][nj] == 1:
                            cnt_house += 1
                # 손익여부 확인 / 서비스 지역내 집의 개수 X 한 집당 비용 >= 운영비용 = 손해가 아닐 때
                if cnt_house * one_cost >= oper_cost:
                    if max_v < cnt_house:
                        max_v = cnt_house
                # 종료조건 / 모든 집을 확인했다면 반복문을 종료한다.
                if cnt_house == all_cnt:
                    flag = 0

        # k값 증가
        k += 1

    print(f'#{tc}', max_v)
