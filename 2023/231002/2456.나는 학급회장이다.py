# import sys
# input = sys.stdin.readline
#
# N = int(input())
# score = [list(map(int, input().split())) for _ in range(N)]
# candidates = [[0, [0, 0, 0]], [0, [0, 0, 0]], [0, [0, 0, 0]]]
#
# max_s = [0, 0]
# for i in score:
#     for j in range(3):
#         candidates[j][0] += i[j]
#         candidates[j][1][i[j] - 1] += 1
#         if max_s[0] < candidates[j][0]:
#             max_s = [candidates[j][0], 1]
#         elif max_s[0] == candidates[j][0]:
#             max_s[1] += 1
#
# temp = []
# for k, i in enumerate(candidates):
#     if max_s[0] == i[0]:
#         temp.append((k, i[1]))
#
# for i in range(3 - 1, 0, -1):
#     if len(temp) == 1:
#         break
#     temp.sort(key=lambda x: x[1][i], reverse=True)
#     max_v = temp[0][1][i]
#     for _ in range(len(temp)):
#         if len(temp) == 1:
#             break
#         k, v = temp.pop(0)
#         if v[i] == max_v:
#             temp.append((k, v))
#
# if len(temp) != 1:
#     print(0, candidates[temp[0][0]][0])
# else:
#     print(temp[0][0] + 1, candidates[temp[0][0]][0])


vote = [list(map(int, input().split())) for _ in range(int(input()))]
vote = list(zip(*vote))
score = [(sum(vote[i]), vote[i].count(3), vote[i].count(2)) for i in range(len(vote))]
score[score.index(min(score, key = lambda x: x[0]))] = (0, 0, 0)
score = list(zip(*score))
chair = 0

for i in range(len(score)):
  if score[i].count(max(score[i])) == 1:
    chair = score[i].index(max(score[i])) + 1
    break

print(chair, max(score[0]))