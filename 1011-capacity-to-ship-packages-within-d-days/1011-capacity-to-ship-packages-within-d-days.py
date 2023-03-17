class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def sumi(x):
            temp = 0
            t = days-1
            for i in weights:
                temp += i
                if temp > x:
                    temp = i
                    t -= 1
            if t >= 0:
                return True
            else:
                return False
        l, h = max(weights),sum(weights)
        fin = 0
        while l <= h:
            mid = l + (h-l)//2
            if sumi(mid):
                h = mid - 1
                fin = mid
            else:
                l = mid + 1 
        return fin
            
            