class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 
        
#         carryon = 0
        
#         digits.reverse()
        
#         for i in range(len(digits)):
            
            
#             if carryon == 1:
                
#                 if digits[i] == 9:
                    
#                     carryon = 1
#                     digits[i] = 0
                    
#                 else:
                    
#                     carryon = 0
#                     digits[i] += 1
#                     break
                    
#             else:
                
#                 if digits[i] == 9:
                    
#                     carryon = 1
#                     digits[i] = 0
#                 else:
#                     carryon = 0
#                     digits[i] += 1
#                     break
#         if carryon == 1:
#             digits.append(1)
            
#         digits.reverse()
        
#         return digits

    
                
                
        