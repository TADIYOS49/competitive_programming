class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for item in words[0]:
            i = 1
            f = len(words)-1
            while i <= f:
                if item not in words[i]:
                    break
                else:
                    words[i] = words[i].replace(item,"",1)
                i += 1
            if i > f:
                ans.append(item)
        return ans
                
        
            