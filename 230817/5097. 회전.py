import sys
sys.stdin = open('input.txt')
#####################################
def enq(data):
    global size
    global front
    global rear
    if (rear + 1) % size == front:
        front = (front + 1) % size
    rear = (rear + 1) % size
    q[rear] = data


T = int(input())
for tc in range(1, T + 1):
    size, cnt = map(int, (input().split()))
    code = list(map(int, input().split()))
    # 큐 사용을 위한 프론트 리어 선언
    front = rear = 0
    # 큐 생성
    q = [0] * size
    print(q)
    # 입력받은 문자열 큐에 추가
    for i in code:
        enq(i)

    # 작업 횟수만큼 반복
    for i in range(cnt):
        # i의 숫자에 해당하는 문자열을 큐에 덮어쓰기
        i = code[i % size]
        print(i)
        enq(i)

    # 마지막에 추가된 데이터 출력
    print(f'#{tc}', q[front])
