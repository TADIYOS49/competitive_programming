from collections import Counter
def solve(arr,m):
    for i in arr:
        if i == "+":
            m += 1
        elif i == "-":
            m -= 1
        if m < 0:
            return False
    if m >= 0:
        return True
    else:
        return False
initial = int(input())
op = input()
l, r = 0, initial
f = 0
count = Counter(op)
while l <= r:
    mid = l + (r-l)//2
    if solve(op,mid):
        f = mid
        r = mid - 1
    else:
        l = mid + 1
print(f+(count["+"]-count["-"]))