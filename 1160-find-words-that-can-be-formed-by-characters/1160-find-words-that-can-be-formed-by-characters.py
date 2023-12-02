class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        thashmap = {}
        sumi = 0
        good = True
        # atach
        for item in chars:
            if item in thashmap:
                thashmap[item] += 1
            else:
                thashmap[item] = 1
        #"cat","bt","hat","tree"
        for word in words:
            tmp = {}
            for item in word:
                if item in tmp:
                    tmp[item] += 1
                else:
                    tmp[item] = 1
            for item in tmp:
                if item not in thashmap:
                    good = False
                    break;
                elif tmp[item] > thashmap[item]:
                    good = False
                    break;
            if good == True:
                sumi += len(word)
            else:
                good = True
            
        return sumi