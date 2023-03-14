class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        res = 1
        def rev(x,b):
            if x == 0:
                return 1
            if x%2 == 0 :
                return rev(x/2,(b*b)%((10**9)+7))
            return rev(x//2,(b*b)%((10**9)+7))*b
        if n%2 == 0:
            res = rev(n//2,20)
        else:
            res = rev((n-1)//2,20)
            res *= 5
        return res%((10**9)+7)
                
                
        
        