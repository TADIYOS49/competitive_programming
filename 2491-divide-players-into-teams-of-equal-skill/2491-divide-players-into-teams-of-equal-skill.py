class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0, len(skill)-1
        temp = skill[l] + skill[r]
        while l<r:
            if temp != skill[l] + skill[r]:
                return -1
            l += 1
            r -= 1
        ans = 0
        l,r = 0, len(skill)-1
        while l < r:
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        return ans
        