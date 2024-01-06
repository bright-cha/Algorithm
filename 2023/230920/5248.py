import sys
sys.stdin = open('input.txt')


def find_set(idx):
    if partner[idx] == 0:
        return True

    partner[idx] = find_set(partner[idx])


T = int(input())
for tc in range(1, T + 1):
    cnt_std, cnt_request = map(int, input().split())
    request = list(map(int, input().split()))

    partner = [999] + [0] * cnt_std
    for i in range(cnt_request):
        v1, v2 = i * 2, i * 2 + 1
        if request[v1] < request[v2]:
            partner[request[v2]] = request[v1]
        else:
            partner[request[v1]] = request[v2]

    cnt = 0

    for i in range(1, cnt_std + 1):
        if find_set(i):
            cnt += 1

    print(f'#{tc}', cnt)

