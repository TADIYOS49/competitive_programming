class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack1 = []
        stack1.append(0)
        count = 0
        for i in s:
            if i == "(":
                stack1.append(0)
            else:
                if stack1[-1] == 0:
                    stack1.pop()
                    stack1[-1] += 1
                else:
                    x = stack1.pop() * 2
                    stack1[-1] += x               
        return stack1[0]
        """
        0 0     
        """
