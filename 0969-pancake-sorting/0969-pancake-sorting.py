class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        i = len(arr) -1
        newmax = max(arr)
        while (i > 0):
            if (arr[i]== i+1):
                i -= 1
                newmax = max(arr[0:i+1])
            elif (arr[i] != i+1 and newmax == arr[0]):
                res.append(newmax)
                arr[0:newmax] = reversed(arr[0:newmax])
            elif (arr[i] != i+1 and newmax != arr[0]):
                x = arr.index(newmax)
                res.append(x+1)
                arr[0:x+1] = reversed(arr[0:x+1])
        return (res)