class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = list(set(nums))
        uni.sort()
        for i in range(len(uni)):
            nums[i] = uni[i]
        return len(uni)