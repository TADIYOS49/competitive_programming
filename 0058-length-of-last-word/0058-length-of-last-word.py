class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        prevalue = True if s[0] != " " else False 
        left = 0
        right = 1
        
        counter = 0
        
        while right < len(s):
            
                
            if s[right] != " " and prevalue == False:
                
                prevalue = True
                left = right
            
            
            elif s[right] == " " and prevalue == True:
                
                prevalue = False
                counter = right - left
                left = right
            
            right += 1
        
        if prevalue:
            counter = right - left
            
        return counter
                
            
                
    
                
                
        
        
        