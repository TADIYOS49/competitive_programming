class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        tot=bricks + ladders
        n=len(heights)-1
        for i in range(n):
            currHeight = heights[i]
            nextHeight = heights[i+1]
            diff=nextHeight-currHeight
            if diff <=  0:
                continue
            heappush(heap,diff)
            if len(heap) > ladders:
                bricks-=heappop(heap)
                if bricks < 0:
                    return i
        return n