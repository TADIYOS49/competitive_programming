class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorts = sorted(intervals)
        res = []
        j = 0
        for i in range(len(sorts)):
            if res == []:
                res.append(sorts[i])
            elif (res[j][1]<sorts[i][0]):
                res.append(sorts[i])
                j+=1
            else:
                res[j][1] = max(res[j][1],sorts[i][1])
        return (res)