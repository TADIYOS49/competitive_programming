class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        res = 0
        cur = 0
        mapping = []
        for i in range(len(position)):
            mapping.append([position[i],speed[i]])
        mapping.sort()
        for i in mapping:
            time.append((target-i[0])/i[1])
        # print(time)
        # print(mapping)
        # print(time[::-1])
        # 1 1 7 3 12
        for x in time[::-1]:
            if x > cur:
                res +=1 
                cur = x
        return res
        # mapping = []
        # count = 0
        # if (sum(speed)%len(speed)==0):
        #     return len(speed)
        # for i in range(len(position)):
        #     mapping.append([position[i],speed[i]])
        # for i in range(target):
        #     res = []
        #     for j in mapping:
        #         j[0] += j[1]
        #     mapping.sort()
        #     for i in range(len(mapping)):
        #         temp = mapping.pop(0)
        #         if res and res[-1][0]==temp[0]:
        #             continue
        #         else:
        #             res.append(temp)
        #     mapping = res
        #     x  = 0
        #     while(mapping):
        #        if (mapping[-1][0]>=target):
        #            mapping.pop()
        #            x += 1
        #            continue
        #        else:
        #            break
        #     if (x>0):
        #         count += 1
        # return count