# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if n == 1:
        #     return 1
        l , h = 0 , n
        while l <= h:
            mid = l + (h-l)//2
            if isBadVersion(mid):
                h = mid - 1
            else:
                l = mid + 1
        return l
        