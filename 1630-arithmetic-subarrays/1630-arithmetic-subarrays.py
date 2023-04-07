class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            check= True
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            diff = arr[1]- arr[0]
            for j in range(2,len(arr)):
                x = arr[j] - arr[j-1]
                if(x != diff):
                    ans.append(False)
                    check = False
                    break
            if check == True:
                ans.append(check)
        return (ans)
        
        
            
            