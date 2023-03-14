class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1
        def rev(x,b):
            if x == 0:
                return 1
            if x%2 == 0 :
                return rev(x/2,(b*b)%((10**9)+7))
            return rev(x//2,(b*b)%((10**9)+7))*b
        return (5**(n%2) * rev(n//2,20))%((10**9)+7)
                
                
        
        