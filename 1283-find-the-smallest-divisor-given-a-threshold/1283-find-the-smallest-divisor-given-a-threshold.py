class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        b = threshold
        def check(x):
            res = []
            for i in nums:
                res.append(ceil(i/x))
            return sum(res)
        l, r = 1, max(nums)
        f = 0
        while l <= r:
            mid = l + (r-l)//2
            if check(mid)<=b:
                r = mid - 1
                f = mid
            else:
                l = mid + 1
        return f
                
        
        