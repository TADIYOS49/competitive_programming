class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        isprime = [True for _ in range(n)]
        isprime[0] = isprime[1] = False
        
        i = 2
        while i * i < n:
            if isprime[i]:
                j = i * i
                while j < n:
                    isprime[j] = False
                    j += i
            i += 1
        count = 0
        for i in isprime:
            if i == True:
                count += 1
        return count
        