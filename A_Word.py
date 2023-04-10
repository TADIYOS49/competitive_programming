var = input()
c = 0
for i in var:
    if i.islower():
        c += 1
    else:
        c -= 1
if c < 0:
    print(var.upper())
else:
    print(var.lower())