class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[(nums1[0]+nums2[0],0,0)]  
        res = []   
        n,m=len(nums1),len(nums2) 
        visited=set((0,0))
        while heap and k:
            summ,i,j=heappop(heap)
            res.append([nums1[i],nums2[j]])
            if j+1<m and (i,j+1) not in visited:
                x1=nums1[i]+nums2[j+1]
                heappush(heap,(x1,i,j+1))
                visited.add((i,j+1))
            if i+1<n and (i+1,j) not in visited:
                x2=nums1[i+1]+nums2[j]
                heappush(heap,(x2,i+1,j))
                visited.add((i+1,j))
            k-=1
        return res