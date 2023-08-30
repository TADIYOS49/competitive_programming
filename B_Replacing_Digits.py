firstnum = list(input())
secondnum = list(input())
ans = []
secondnum.sort()
for i in firstnum:
    if secondnum and secondnum[-1] > i:
        ans.append(secondnum[-1])
        secondnum.pop()
    else:
        ans.append(i)

print("".join(ans))
