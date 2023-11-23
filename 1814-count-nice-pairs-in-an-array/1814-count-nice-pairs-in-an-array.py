class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
    
        def rev(n, rn = 0):
            while n != 0:
                
                digit = n % 10
                rn = rn * 10 + digit
                n //= 10
        
            return rn
        
        mod = (10**9) + 7
        dic = {}
        count_total = 0
        for num in nums:
            diff = num - rev(num)
            if diff not in dic:
                dic[diff] = 0
                
            count_total = (count_total + dic[diff]) % mod

            dic[diff] += 1
            
        return count_total