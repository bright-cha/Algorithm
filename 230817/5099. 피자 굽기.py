import sys
sys.stdin = open('input.txt')
######################################
def enQueue(data):
    global rear
    rear = (rear+1) % size
    oven[rear] = data


def deQueue():
    global front
    global oven
    front = (front+1) % size


def qPeek():
    return oven[front]


T = int(input())
for tc in range(1, T + 1):
    size, pizza_cnt = map(int, input().split())
    pizza = list(map(int, input().split()))
    idx = 0
    rear = 0
    front = 0
    oven = [[0, 0] for _ in range(size)]
    complete = 0
    while complete < pizza_cnt:
        # 구워야 하는 피자가 있고, 화덕이 가득 차지 않았다면 피자를 넣어준다.
        if pizza and not((rear + 1) % size == front):
            enQueue([pizza.pop(0), idx])
            idx += 1
            continue
        if qPeek()[0] == 0:
            deQueue()
            complete += 1
            continue
        elif qPeek()[0] > 0:
            qPeek()[0] //= 2
            rear = (rear + 1) % size
            front = (front + 1) % size
            continue

    print(f'#{tc}', max(oven)[1], oven)
