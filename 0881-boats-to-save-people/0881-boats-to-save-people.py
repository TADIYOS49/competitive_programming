class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        counter = 0
        while l <= r:
            if people[l] + people[r]>limit:
                counter += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                counter += 1
                l += 1
                r -= 1
        return counter    