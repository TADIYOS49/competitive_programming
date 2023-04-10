from collections import defaultdict
def solve(nums,k):
    dicti = {}
    for x in nums:
        if x in dicti:
            dicti[x] += 1
        else:
            dicti[x] = 1
    l = 0
    r = 1
    res = []
    nums.sort()
    for x in range(len(nums)):
        if nums[x] - nums[x-1] == 0 or nums[x] - nums[x-1] == 1:
            if dicti[nums[l]] >= k and dicti[nums[x]] >= k:
                res.append([[nums[x]-nums[l]],[nums[l],nums[x]]])
            if dicti[nums[x]] < k:
                l = x + 1
        else:
            l = x 
    res.sort()
    if res == []:
        return []
    else:
        return res[-1][1]
tests = int(input())
for _ in range(tests):
    length , k = map(int, input().split())
    arr  = list(map(int, input().split()))
    answer = solve( arr, k )
    if not len(answer):
        print(-1)
    else:
        print(*answer)