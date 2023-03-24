class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(x,m):
            while m <= len(citations)-1:
                if citations[m] < x:
                    return False
                m += 1
            return True
        l, r = 0, len(citations)-1
        f = 0
        while l <= r:
            mid = l + (r-l)//2
            if check(len(citations)-mid,mid):
                f = len(citations)-mid
                r = mid - 1
            else:
                l = mid + 1
        return f
                
                
            
        