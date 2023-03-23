import collections 
class Solution: 
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int: 
        # count = 0
        tick = collections.deque([])  
        for i in tickets: 
            tick.append(i) 
        # for i in range(tick[k]):
        #     j = 0
        #     while(j<len(tick)):
        #         count += 1
        #         temp = tick.popleft() - 1
        #         if temp !=0:
        #             tick.append(temp)
        #         j += 1
        # return count
        count = 0
        summ = sum(tick) 
        for i in range(summ): 
            if tick[k] == 1 and k == 0:
                count += 1 
                break 
            temp = tick.popleft() - 1 
             
            #print(temp) 
             
            if (k == 0): 
                k = len(tick)
            else: 
                k -= 1 
            if temp != 0: 
                tick.append(temp) 
            count += 1 
        return count     
     
        """ 
         output 5 
        5 2 1 1  k = 1 
         
        2 1 1 4  k = 1 
        1 1 4 1  k = 2 
        1 4 1 0  k = 3  
        4 1 0 0  k = 4 
        1 3 0 0  k  = 5  
         
         
        3 0 0 0  k  = 6  
                        
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
        """