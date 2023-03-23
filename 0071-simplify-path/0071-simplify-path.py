class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        stack1 = []
        for i in stack:
            if i == '':
                continue
            elif i == '..':
                if stack1:
                    stack1.pop()
            elif i == ".":
                continue
            else:
                stack1.append(i)
        res = "/" + "/".join(stack1)
        return res
                


            

    