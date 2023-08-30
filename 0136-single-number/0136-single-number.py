class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final = 0
        for i in nums:
            final ^= i
        return final