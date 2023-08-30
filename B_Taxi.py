gl = int(input())
gnum = list(map(int,input().split()))
gsum = sum(gnum)
def check(n):
    if gsum/n > 4:
        return False
    else:
        return True
l,r = 1,gl
final = 0
while l <= r:
    mid = l + (r-l)//2
    if check(mid):
        final = mid
        r = mid - 1
    else:
        l = mid + 1
print(final)
