class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if (len(changed)% 2 != 0):
            return([])
        count = [0] * 100001
        ans =[]
        for x in changed:
            count[x] += 1
        changed.sort()
        if (count[0]%2) != 0:
            return([])
        for x in range((len(count) // 2)+1):
            for y in range(count[x]):
                if count[x*2] != 0 :
                    ans.append(x)
                    count[x] -= 1
                    count[x*2] -= 1
                elif (x!=0):
                    return ([])
        return(ans)