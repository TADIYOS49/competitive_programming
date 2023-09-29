class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        if len(nums) < 3:
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = bisect.bisect_left(nums,nums[i]+nums[j])
                if k - j - 1 > 0:
                    count += k - j - 1
        return count
    
        