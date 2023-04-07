class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        ran = len(piles) // 3
        for x in range(1,len(piles),2):
            if ( ran != 0):
                ans += piles[x]
                ran -= 1
        return ans