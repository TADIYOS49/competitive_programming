inp = input()
t = 0
for i in inp:
    if i == '4' or i == '7':
        t += 1
if t == 4 or t == 7:
    print("YES")
else:
    print("NO")