class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(locked)
        if n%2 is 1: # Obviously this results in an imbalance of parantheses
            return False
        unlockedSlots = 0
        unlockedLefts = 0 #Unlocked slots currently used to match lefts
        unmatchedLefts = 0 #Lefts that haven't found a match
        for i in range(n):
            if locked[i] is '0':
                if unmatchedLefts > 0:
                    unlockedLefts += 1
                    unmatchedLefts -= 1
                unlockedSlots += 1
            else: # locked[i] is 1
                if s[i] is '(':
                    unmatchedLefts += 1
                elif s[i] is ')':
                    if unmatchedLefts is 0 and unlockedSlots is 0:
                        return False
                    elif unmatchedLefts > 0:
                        unmatchedLefts -= 1
                    elif unlockedSlots > unlockedLefts: 
                        unlockedSlots -= 1
                    else:
                        unmatchedLefts += 1
                        unlockedSlots -= 1
        if unmatchedLefts > 0:
            return False
        return True

            