inp = input()
ans = 0
for i in inp:
    if i in "HQ9":
        ans = 1
if ans == 1:
    print("YES")
else:
    print("NO")