class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        sumi = 0
        for item in nums:
            
            sumi += item
            prefix.append(sumi)
        
        return prefix
            
        