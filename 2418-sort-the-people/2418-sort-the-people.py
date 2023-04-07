class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        couple = []
        for i in range(len(names)):
            couple.append([heights[i],names[i]])
        couple.sort(reverse=True)
        ans = []
        for i in couple:
            ans.append(i[1])
        return ans