class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        totaltime = []
        for ind in range(len(plantTime)):
            totaltime.append([growTime[ind],plantTime[ind]])
        totaltime.sort(reverse=True)
        sumi = 0
        minday = 0
        for ind in totaltime:
            temp = ind[0] + sumi + ind[1]
            sumi += ind[1]
            minday = max(minday,temp)
        return minday