class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(x):
            t = 0
            for i in piles:
                t += ceil(i/x)
            # print(t,h)
            return h >= t
        l , hi = 1, max(piles)
        f = 0
        while l <= hi:
            mid = l + (hi-l)//2
            # print(check(mid))
            # print(mid)
            if check(mid):
                hi = mid - 1
                f = mid
            else:
                l = mid + 1
        return f
                
                
        