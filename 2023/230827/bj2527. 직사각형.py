for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    square1 = [x1, y1, p1, q1]
    square2 = [x2, y2, p2, q2]

    rst= 'd'
    for i in range(x1, p1 + 1):
        if x2 <= i <= p2:
            if y2 <= y1 <= q2 or y2 <= q1 <= q2:
                rst = 'a'
                break
        else:
            if y2 <= y1 <= q2 or y2 <= q1 <= q2:
                pass