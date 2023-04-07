class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums)//2):
            ans.append(nums[i]+nums[len(nums)-1-i])
        return (max(ans))