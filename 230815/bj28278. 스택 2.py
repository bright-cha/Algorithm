import sys
sys.stdin = open('input.txt')
###################################################
T = int(input().strip())
for tc in range(1, T + 1):
    size = int(input().strip())
    maze = [list(map(int, input().strip())) for _ in range(size)]
    # 경로 유무 - 실패 기본값
    clear = 0

    # 방문기록지
    visited = [[0] * size for _ in range(size)]

    # 빈 스택 생성
    stack = []

    # 출발지점 찾기
    for i in maze:
        if 2 in i:
            x = maze.index(i)
            y = i.index(2)
            # 출발지 스택에 추가
            stack.append((x, y))
            # 출발지점도 통로기 때문에 0으로 변경
            maze[x][y] = 0
            break

    # 통로파악을 위한 델타 생성
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    # 3을 찾은 경우를 위한 깃발 플래그
    flag = True
    # 스택이 비어있지 않다면 진행
    while stack and flag:
        # 현재 위치 설정
        x, y = stack[-1]

        # 통로 탐색
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < size and 0 <= ny < size:
                # 도착지라면 clear 값과 flag 값 변경
                if maze[nx][ny] == 3:
                    clear = 1
                    flag = False
                    break
                # 통로이면서 방문기록이 없다면 stack 추가
                elif not maze[nx][ny] and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1
                    break
        # 통로가 없다면 이전 갈림길로 돌아간다.
        else:
            stack.pop()

    print(f'#{tc}', clear)
