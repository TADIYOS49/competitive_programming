class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)-1):
            if ((nums[i-1]<=nums[i] & nums[i]<=nums[i+1]) or (nums[i-1]>=nums[i] & nums[i]>=nums[i+1])):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        return (nums)