class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        qn = []
        wn = []
        for i in queries:
            query = Counter(i)
            smallest = min(query.keys())
            qn.append(query[smallest])
        for i in words:
            word = Counter(i)
            smallest = min(word.keys())
            wn.append(word[smallest])
        wn.sort()
        for i in qn:
            f = len(wn)
            l, h = 0, len(wn)-1
            while l<=h:
                mid = l + (h-l)//2
                if wn[mid] <= i:
                    l = mid + 1
                if wn[mid] > i:
                    f = mid
                    h = mid - 1
            ans.append(len(wn)-f)
        return ans
            
                
                
                    