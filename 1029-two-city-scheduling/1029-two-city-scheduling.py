class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # [10,20], [30, 200], [400, 50], [30, 20]
        # a-b
        # -10, -170, 350, 10
        # -170, -10, 10, 350
        # 30,200 - 10, 20 - 30, 20 - 400, 50
        costs.sort(key = lambda x: x[0]-x[1])
        mid = len(costs)//2
        return sum([x[0]  for x in costs[:mid]  ]) + sum([x[1]  for x in costs[mid:]  ])