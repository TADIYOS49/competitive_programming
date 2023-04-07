class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        ans = []
        for x in range(len(points)):
            res.append(((pow(points[x][0],2) + pow(points[x][1],2)),points[x]))
        res.sort()
        for x in range(k):
            ans.append(res[x][1])
        return (ans)

            