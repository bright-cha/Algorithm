

# def deq():
#     global front
#     front = (front + 1) % len(N)
#     return N[front]
#
#
# N = [i for i in range(1, int(input().strip()) + 1)]
# front = 0
# while len(N) > 1:
#     N.pop(front)
#     deq()
#
# print(*N)

from collections import deque

N = deque([i for i in range(1, int(input().strip()) + 1)])
while len(N) != 1:
    N.popleft()
    N.append(N.popleft())

print(*N)
