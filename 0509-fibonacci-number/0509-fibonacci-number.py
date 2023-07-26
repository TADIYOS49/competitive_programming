class Solution:
    def fib(self, n: int) -> int:
        memo = {}
    
        def fab(i):
            if i <= 1: 
                return i
            if i in memo:
                return memo[i]

            result = fab(i - 1) + fab(i - 2)
            memo[i] = result   
            return result 
        
        return fab(n)
