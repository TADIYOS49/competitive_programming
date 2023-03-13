class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = ceil(len(s)/2)
        l = 0
        r = len(s)-1
        def rev(l,r):
            if l == i:
                return 
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            return rev(l,r)
        rev(l,r)
            