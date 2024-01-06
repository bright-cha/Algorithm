import sys
sys.stdin = open("input.txt", "r")
#########################################
T = int(input())
for tc in range(1, T+1):
    tc_num, length = input().split()
    length = int(length)
    outside_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
                   "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    nums = list(input().split())

    cnt = [0] * 10
    for i in nums:
        cnt[outside_num[i]] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i-1]

    rst = [[''] for _ in range(length)]
    for i in range(length-1, -1, -1):
        cnt[outside_num[nums[i]]] -= 1
        rst[cnt[outside_num[nums[i]]]] = nums[i]

    print(tc_num)
    print(*rst)
