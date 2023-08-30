class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sumi = []
        if len(a) > len(b):
            temp = a
            a = b
            b = temp
        added = ["0"] * (len(b)-len(a))
        a = "".join(added) + a
        # print(a,b)
        i = len(a)-1
        while i >= 0:
            # print(a[i],b[i],carry, sumi)
            if carry == 0:
                carry = int(a[i]) & int(b[i])
                sumi.append(str(int(a[i])^int(b[i])))
            else:
                bitsum = int(a[i]) ^ int(b[i]) ^ carry
                sumi.append(str(bitsum))
                if int(a[i]) | int(b[i]) == 0:
                    carry = 0        
            i -= 1
        if carry == 1:
            sumi.append("1")
        return "".join(sumi[::-1])