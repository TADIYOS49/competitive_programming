class Solution:
    def splitString(self, s: str) -> bool:
        """
        050043
        0 fun(50043)
        5 fun(0043)
        
        """
        #ans = False
        # def check(x,s,pre):
        #     left = int(s[0:x+1])
        #     right = int(s[x+1:])
        #     if left - right == 1:
        #         return True
        #     else:
        #         return False
        def solve(s,prev):
            if int(prev) - int(s)== 1:
                return True
            for i in range(1,len(s)):
                curr = s[0:i]
                if (int(prev) - int(curr)) == 1 and solve(s[i:],curr):
                    return True
            return False
        for j in range(1,len(s)):
            if solve(s[j:],int(s[0:j])):
                return True
        return False
    
    