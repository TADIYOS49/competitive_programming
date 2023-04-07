class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        ans = []
        for i in count:
            res.append([count[i],i])
        res.sort(reverse=True)
        for i in range(k):
            ans.append(res[i][1])
        return (ans)
