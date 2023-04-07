class Solution:
    def sortColors(self, nums: List[int]) -> None:
        x = 0
        count = [0] * 3
        for i in nums:
            count[i] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                nums[x] = i
                x += 1
        