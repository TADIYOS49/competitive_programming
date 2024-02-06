class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        occurance = []
        
        for item in range(0,len(haystack)):
            
            if haystack[item] == needle[0]:
                occurance.append(item)
        
        
        for item in occurance:
            
            finalpoint = item+len(needle)
            
            if haystack[item:finalpoint] == needle:
                return item
            
        return -1
            
        
        
            
                    