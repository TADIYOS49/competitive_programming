class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = list(range(1,n+1))
        self.k = k
        self.n = n
        b = Solution.calc(self,x,0,1)
        return b[0]
    def calc(self,x,i,count)->int:
        if len(x) == 1:
            return x
        if count == self.k:
            x.remove(x[i])
            count = 1
            i -= 1
        elif count < self.k:
            count += 1
        if i >= len(x) - 1:
            i = -1
        return Solution.calc(self,x,i+1,count)
