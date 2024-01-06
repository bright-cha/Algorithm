T = int(input())
for tc in range(1, T + 1):
    nums_length = int(input())
    nums = list(map(int, input().split()))
    sort_nums = [0] * nums_length
    max_num = 0
    for i in nums:
        if max_num < i:
            max_num = i

    cnt = [0] * (max_num + 1)

    for i in nums:
        cnt[i] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    for i in range(nums_length - 1, -1, -1):
        cnt[nums[i]] -= 1
        sort_nums[cnt[nums[i]]] = nums[i]

    print(f'#{tc} {" ".join(map(str, sort_nums))}')
