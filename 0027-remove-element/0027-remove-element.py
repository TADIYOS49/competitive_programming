class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = 51
                k += 1
        nums.sort()
        print(nums)
        return len(nums) - k
        
        