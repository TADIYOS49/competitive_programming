class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def fun(i):
            if i > len(cost)-1:
                return 0
            if i in memo:
                return memo[i]
            onestep = fun(i+1) + cost[i]
            twostep = fun(i+2) + cost[i]
            memo[i] = min(onestep,twostep)
            return min(onestep,twostep)
        return min(fun(0),fun(1))
        