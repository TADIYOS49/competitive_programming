class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            res.append(i)
            if (i == "*" or i == "+" or i == "/" or i == "-"):
                operand = res.pop()
                item1 = res.pop()
                item2 = res.pop()
                if (operand == "/"):
                    x = eval(item2+operand+item1)
                    if (x<0):
                        x = ceil(x)
                    elif(x>=0):
                        x = floor(x)
                    res.append(str(x))
                else:
                    res.append(str(eval(item2+operand+item1)))
        return int(res[0])