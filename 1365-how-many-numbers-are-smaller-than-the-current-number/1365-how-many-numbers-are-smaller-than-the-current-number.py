class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        ans = []
        for i in nums:
            ans.append(x.index(i))
        return ans
    
        