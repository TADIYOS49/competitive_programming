class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , h = 0 , len(nums)-1
        first = -1
        last = -1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                h = mid  - 1
                first = mid
        l , h = 0, len(nums)-1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid  + 1
                last = mid
        return [first,last]
                