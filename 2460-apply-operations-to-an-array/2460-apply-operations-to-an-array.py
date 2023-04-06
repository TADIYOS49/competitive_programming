class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        res = []
        zero = []
        for i in nums:
            if i != 0:
                res.append(i)
            else:
                zero.append(i)
        return res+zero