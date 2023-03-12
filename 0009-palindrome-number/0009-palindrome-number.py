class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        l = 0
        r = len(num)-1
        while l < r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1
        return True
