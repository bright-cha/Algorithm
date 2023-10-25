from collections import deque

N = int(input())
form = list(input())

# stack = deque([])
# for i in form:
#     stack.append(i)
#     if len(stack) == 3:

# def back(idx, v, lst):
#     if idx == N:
#         return
#
#     if idx % 3 == 0:
#         lst = deque(lst)
#         temp = 0
#         while lst:
#             i = lst.popleft()
#             if i in ['+', '-', '*']:
#                 lst.append(i)
#                 continue
#             elif temp == 0:
#                 temp = int(i)
#             else:
#                 oper = lst.popleft()
#                 if oper == '+':
#                     temp = temp + int(i)
#                 if oper == '-':
#                     temp = temp - int(i)
#                 if oper == '*':
#                     temp = temp * int(i)
#         back(idx + 1, v + temp, lst)
#     else:
#         back(idx + 1, v, lst + [form[idx]])
