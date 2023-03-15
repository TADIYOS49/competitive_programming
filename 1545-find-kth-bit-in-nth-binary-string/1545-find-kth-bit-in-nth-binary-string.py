class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        self.past = {}
        def reverse(x):
            return x[::-1]
        def invert(x):
            temp = ""
            for i in x:
                if i == "1":
                    temp += "0"
                else:
                    temp += "1"
            return temp
        def rec(n):
            if n == 1:
                return "0"
            if n in self.past:
                return self.past[n]
            self.past[n] = rec(n-1) + "1" + reverse(invert(rec(n-1)))
            return self.past[n]
        res = rec(n)
        return res[k-1]
        