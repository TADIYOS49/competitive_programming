class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n2 = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                if n2 > len(nums2)-1:
                    break
                nums1[i] = nums2[n2]
                n2 += 1
        nums1.sort()
        