class Solution:
    def climbStairs(self, n: int) -> int:
        
        prevcomp = {}
        
        def fun(x):
            
            if x == 0:
                return 1
            if x < 0:
                return 0
            
            if x in prevcomp:
                return prevcomp[x]
            
            else:
                prevcomp[x] = (fun(x-1)+fun(x-2))
            
            return prevcomp[x]
        
        return fun(n)
        