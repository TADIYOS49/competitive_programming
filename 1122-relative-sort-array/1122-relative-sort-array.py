class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        notin = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    res.append(j)
        for i in arr1:
            if i not in arr2:
                notin.append(i)
        notin.sort()
        return(res+notin)