class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        nran = [i for i in range(1,n+1)]
        def solve(self,start,visited):
            if start == len(nran):
                self.ans += 1
                #print(visited)
                return 
            for i in range(0,len(nran)):
                if nran[i] not in visited and ((i+1)%nran[start] == 0 or nran[start]%(i+1) == 0):
                    visited.add(nran[i])  
                    solve(self,start+1,visited)
                    visited.remove(nran[i])
        solve(self,0,set())
        return self.ans
        """
        1,2,3
        """
            