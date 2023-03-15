class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def rec(x,i,f,flag,sump1,sump2):
            if i > f:
                return sump1 >= sump2
            if flag:
                return rec(x,i+1,f,False,sump1+x[i],sump2) or rec(x,i,f-1,False,sump1+x[f],sump2)
            else:
                return rec(x,i+1,f,True,sump1,sump2+x[i]) and rec(x,i,f-1,True,sump1,sump2+x[f])
        return rec(nums,0,len(nums)-1,True,0,0)