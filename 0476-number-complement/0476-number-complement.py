class Solution:
    def findComplement(self, num: int) -> int:
        check = 1
        res = num
        while check <= num:
            res = res ^ check
            check = check << 1
        return res
        """
        00000...101
        1 1111...010
        """