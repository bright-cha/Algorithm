from collections import deque


def bfs(num):
    # 100만 이하 동일한 숫자 가지치기를 위한 리스트 초기화
    visited = [0] * 10000001
    # bfs를 위한 큐 생성 / 숫자, 횟수
    que = deque([(num, 0)])
    # 현재 숫자 방문 표시
    visited[num] = 1

    while que:
        # 저장된 숫자와 횟수 가져오기
        num, cnt = que.popleft()
        # 목표 숫자라면 리턴
        if num == end:
            return cnt
        # 아니라면
        else:
            # 연산실행
            for i in calculate:
                # 2인경우 곱하기
                if i == 2:
                    # 계산된 숫자를 처음 만나고 100만 이하라면 방문 표시 후 큐에 추가
                    temp = num * 2
                    if visited[temp] == 0 and 0 < temp <= 1000000:
                        visited[temp] = 1
                        que.append((temp, cnt + 1))
                # 그 외는 i 값 더하기
                else:
                    temp = num + i
                    # 계산된 숫자를 처음 만나고 100만 이하라면 방문 표시 후 큐에 추가
                    if visited[temp] == 0 and 0 < temp <= 1000000:
                        visited[temp] = 1
                        que.append((temp, cnt + 1))


T = int(input())
for tc in range(1, T + 1):
    # 출발숫자, 목표숫자
    start, end = map(int, input().split())
    # 계산
    calculate = [1, -1, -10, 2]

    print(f'#{tc}', bfs(start))