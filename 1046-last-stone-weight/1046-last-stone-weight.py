class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #first sort the list
        stones.sort()

        while stones:
            #most heaviest stone
            s1 = stones.pop()

            #if list is empty after removing one stone i.e s1 then 
            #return s1
            if not stones: return s1

            #second heaviest stone s2 where s2 <= s1
            s2 = stones.pop()

            #if s1 > s2 then element to be inserted is s1-s2 as given in the 
            #problem statement
            if s1 > s2:

                #using Insort_left Function Of Bisect Module
                #we will insert s1-s2 at correct position 
                insort_left(stones, s1-s2)

            #else s1 == s2 and as we are continously popping elements 
            #both the stones are destroyed if they are same

        #if no more stones remaining return 0 
        return 0 
