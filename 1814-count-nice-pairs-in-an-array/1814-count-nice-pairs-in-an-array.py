class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        equalities = {}
        total_count = 0
        
        def rev(n,rn = 0):
            
            while n != 0:
                digit = n % 10
                rn = rn * 10 + digit
                n //= 10
                
            return rn
        
        for num in nums:
            tmp = num - rev(num)
            if tmp not in equalities:
                equalities[tmp] = 1
            else:
                equalities[tmp] += 1
        #print(equalities)        
        
        for index in equalities:
            tmp = equalities[index]
            if tmp > 1:
                nominator = math.factorial(tmp)
                denominator = 2 * (math.factorial(tmp-2))
                count = nominator // denominator
                total_count += count 
                # total_count += floor(math.factorial(tmp) / 2*(math.factorial(tmp - 2)))
                #print(index,total_count,tmp)
            
        return total_count % (10**9 + 7)