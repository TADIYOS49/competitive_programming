class Solution:
    def findKthBit(self, n: int, k: int) -> str:
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
            return rec(n-1) + "1" + reverse(invert(rec(n-1)))
        res = rec(n)
        return res[k-1]
        