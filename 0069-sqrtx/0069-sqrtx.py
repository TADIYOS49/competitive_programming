class Solution:
    def mySqrt(self, x: int) -> int:
        l , h = 1 , x
        while l <= h:
            mid = l + (h-l)//2
            #print(mid * mid)
            if (mid * mid) > x:
                h = mid - 1
            elif (mid * mid) < x:
                l = mid + 1
            else:
                return mid
        return l - 1
        