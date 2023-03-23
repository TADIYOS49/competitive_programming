class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicti = collections.defaultdict(int)
        l = r = 0
        maxi = 0
        while r < len(s):
            dicti[s[r]] += 1
            while dicti[s[r]] != 1:
                dicti[s[l]] -= 1
                if not dicti[s[l]]:
                    dicti.pop(s[l])
                l += 1
            maxi = max(maxi,len(dicti))
            r += 1
        return maxi