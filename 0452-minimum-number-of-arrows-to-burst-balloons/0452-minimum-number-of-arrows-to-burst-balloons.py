class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 1
        checker = points[0][1]
        for i in range(1,len(points)):
            if checker < points[i][0]:
                checker = points[i][1]
                ans += 1
            else:
                checker = min(points[i][1],checker)
        return ans
                
                
        
        