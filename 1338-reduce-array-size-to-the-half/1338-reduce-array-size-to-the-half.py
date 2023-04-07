class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = [0] * (pow(10,5) + 1)
        su = 0
        res = 0
        for x in arr:
            count[x] += 1
        half = len(arr) // 2
        count.sort(reverse = True) 
        i = 0
        while(su < half):
            su += count[i]
            i += 1   
        return i