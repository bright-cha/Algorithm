'''# Queue 1
def enQ(data):
    global rear
    if rear == Qsize - 1: # 가득 차면
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:
        print('Q가 비었다.')
        return
    else:
        front += 1
        return Q[front]


Qsize = 3
Q = [0] * 3
rear = front = -1
enQ(1)
enQ(2)
rear += 1
Q[rear] = 3

# 모든 내용 꺼내기
# while front != rear:
#     front += 1
#     print(Q[front])

enQ(4)
print(deQ())
print(deQ())
front += 1
print(Q[front])
print(deQ())
'''
# 원형 큐
def enq(data):
    global rear
    global front
    if (rear + 1) % cQsize == front:
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data


def deq():
    global front
    if rear == front:
        print('비어있습니다.', end=' ')
        return
    else:
        front = (front + 1) % cQsize
        return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = rear = 0

enq(1)  # 1
enq(2)  # 2
enq(3)  # 3
enq(4)  # 0
enq(5)  # 1
print(deq())  # 2
print(deq())  # 3
print(deq())  # 0
print(deq())  # 1
