n = input().strip()
n = n.replace("144", "a")
n = n.replace("14", "b")
n = n.replace("1", "c")
final = True
for i in set(n):
    if i not in "abc":
        final = False
        break
if final:
    print("YES")
else:
    print("NO")
