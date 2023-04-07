class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(l,r,items):
            if len(items) == k:
                ans.append(items.copy())
                return
            for i in range(l,r+1):
                items.append(i)
                solve(i+1,r,items)
                items.pop()
        solve(1,n,[])
        return ans
        
        