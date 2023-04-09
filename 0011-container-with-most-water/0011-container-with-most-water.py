class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        ans = 0
        x = 0
        while i <= j:
            if (height[i]<height[j]):
                x = height[i]
                ans = max(ans, x * (j-i))
                i +=1
            else:
                x = height[j]
                ans = max(ans, x * (j-i))
                j -=1 
        return ans