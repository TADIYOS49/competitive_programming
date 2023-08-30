class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        
        1,2,3,4,5,10
        1,2,3,4,5,5
        
        """
        piles = list(map(lambda x : -x , piles))
        heapify(piles)
        
        while k > 0 and piles:
            temp = heappop(piles) * -1
            temp = temp - floor(temp/2)
            if temp != 0:
                heappush(piles,-1 * temp)
            k -= 1
        return sum(piles) * -1