def solve(x,y):
    return min((x+y)//4,x,y)
    # l, h = 0, (x+y)//4
    # f = 0
    # while l<=h:
    #     mid = l + (h-l)//2
    #     if mid > min(x,y):
    #         h = mid - 1
    #     if mid <= min(x,y):
    #         l = mid + 1
    #         f = mid
    # return f
tests = int(input())
for _ in range(tests):
    a,b = map(int,input().split())
    print(solve(a,b))
