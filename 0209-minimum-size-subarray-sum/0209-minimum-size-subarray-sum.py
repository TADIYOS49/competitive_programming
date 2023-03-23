class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,sumi = 0,0
        res = float("inf")
        for r in range(len(nums)):
            sumi += nums[r]
            while sumi >= target:
                res = min(res,r-left+1)
                sumi-=nums[left]
                left +=1
        if res == float("inf"):
            return 0
        else:
            return res
            

            
