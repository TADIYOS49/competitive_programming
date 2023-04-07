class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        check = len(nums)//3
        count = Counter(nums)
        for i in count.keys():
            temp = count[i]
            if temp > check:
                ans.append(i)
        return ans
        