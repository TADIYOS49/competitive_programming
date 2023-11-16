class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        collect = set()
        
        for item in nums:
            tmp = int(item,2)
            collect.add(tmp)
            
        #print(collect) 
        n = pow(2,len(nums))
        
        for i in range(n):
            if i not in collect:
                ans = bin(i)
                ans = ans[2:]
                leng = len(nums[0]) - len(ans)
                tmp = ""
                while leng > 0:
                    tmp += "0"
                    leng -= 1
                ans = tmp + ans
                return ans
            
            
        