import sys
sys.stdin = open('input.txt')
######################################
def enQueue(data):
    global rear
    rear = (rear+1) % size
    oven[rear] = data


def deQueue():
    global front
    front = (front+1) % size
    return oven[front]


T = int(input())
for tc in range(1, T + 1):
    size, pizza_cnt = map(int, input().split())
    size += 1
    pizza = list(map(int, input().split()))
    # pizza = [[i, v] for i, v in enumerate(pizza)]
    rear = 0
    front = 0
    complete = 0
    oven = [0] * size

    idx = 0
    while complete < pizza_cnt:
        # 구워야 하는 피자가 있고, 화덕이 가득 차지 않았다면 피자를 넣어준다.
        if pizza and not((rear + 1) % size == front):
            enQueue([pizza.pop(0), idx])
            idx += 1
            continue

        check = deQueue()
        if check[0] < 2:
            complete += 1
        else:
            check[0] //= 2
            enQueue(check)
    print(f'#{tc}', oven[front][1]+1)
