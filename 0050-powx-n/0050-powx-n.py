class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(n,ans):
            if n == 0:
                return 1
            if n%2 == 0:
                return rec(n/2,ans*ans)
            return rec((n-1)/2,ans*ans)*ans
        if n >= 0:
            return rec(abs(n),x)
        else:
            x = rec(abs(n),x)
            return 1/x
                