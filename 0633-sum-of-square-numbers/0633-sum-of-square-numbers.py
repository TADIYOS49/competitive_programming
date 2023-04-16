class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, h = 0, c
        final = 0
        while l <= h:
            mid = l + (h-l)//2
            if (mid*mid) >= c:
                #print(mid)
                final = mid
                h = mid - 1
            else:
                l = mid + 1
        #print(final)
        if (final*final) == c:
            return True
        l, r = 0,final-1
        while l <= r:
            temp = (l*l) + (r*r)
            if temp < c:
                l += 1
            elif temp > c:
                r -= 1
            else:
                return True
        return False
                
            
        