def enq(data):
    global snak
    global rear
    snak -= 1
    rear = (rear + 1) % q_size
    q[rear] = data


def deq():
    global front
    front = (front + 1) % q_size
    return q[front]


q_size = 20
q = [0] * q_size
front = rear = 0

snak = 20
human = 0

flag = 1
while flag and snak:
    human += 1
    enq(human)
    deq()
    for _ in range(human + 1):
        if snak == 0:
            flag = 0
            break
        enq(human)

print(deq())