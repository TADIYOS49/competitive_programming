class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j = 0, len(nums)-1
        nums.sort()
        count = 0
        for x in range(len(nums)):
            if i >= j:
                break
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return count
            
