class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1,1]
        def rev(x,i,res):
            if i == x:
                return res
            temp = []
            for j in range(1,len(res)):
                temp.append(res[j]+res[j-1])
            res = [1] + temp + [1]
            return rev(x,i+1,res)
        res = rev(rowIndex,1,res)
        return res