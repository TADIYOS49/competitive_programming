class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r = 0,1
        res= []
        count = 1
        while l < len(chars)-1 and r <len(chars):
            if chars[l] != chars[r]:
                res.append(chars[l])
                if count > 1:
                    temp = str(count)
                    if len(temp) > 1:
                        for i in temp:
                            res.append(i)
                    else:
                        res.append(temp)
                count = 0
            l += 1
            r += 1
            count += 1
        res.append(chars[l])
        if count > 1:
            temp = str(count)
            for i in temp:
                res.append(i)
                
        # if len(chars) == 1:
        #     return 1
        # dicti = Counter(chars)
        # res = []
        # for i in chars:
        #     if i not in res:
        #         res.append(i)
        #         if dicti[i] != 1:
        #             if dicti[i] > 9:
        #                 temp = str(dicti[i])
        #                 for j in temp:
        #                     res.append(j)
        #             else:
        #                 res.append(str(dicti[i]))
        # l = 0
        # r = 0
        # res = ""
        # while r < len(chars):
        #     if chars[l] == chars[r]:
        #         r += 1
        #     elif chars[l] != chars[r]:
        #         res += chars[l]
        #         if r-l != 1:
        #             res += str(r-l)  
        #         l = r
        #         r += 1
        #     if r == len(chars)-1:
        #         res += chars[l]
        #         if r-l+1 != 1:
        #             res += str(r-l+1)
        #         l = r
        #         r += 1   
        chars[::] = res[::]
        return len(chars)     
        # for i in d:
        #     res += str(i)
        #     if d[i] != 1:
        #         res += str(d[i])        
        # chars[::] = res[::]
        # print(chars) 
        # return len(res)