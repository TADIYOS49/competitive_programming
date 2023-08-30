class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(ans,matrix[i][j])
        while k > 1:
            heappop(ans)
            k -= 1
        return ans[0]
                