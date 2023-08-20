import sys

sys.stdin = open('input.txt')


#####################################
def cooking():
    cooking_time = 0
    snack = 0
    while people:
        if cooking_time in people:
            while people and people[0] == cooking_time:
                people.pop(0)
                snack -= 1
                if snack < 0:
                    return 0
        cooking_time += 1
        if (cooking_time % second) == 0:
            snack += cnt
    return 1


T = int(input())
for tc in range(1, T + 1):
    n_people, second, cnt = map(int, input().split())
    people = list(map(int, input().split()))
    # 범죄 검거
    people.sort()
    waiting = []

    rst = cooking()
    if rst == 1:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
