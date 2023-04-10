l = int(input())
x = 0
stack = []
for i in range(l):
    s = input()
    if s == 'add':
        x += 1
        if x >= 2**32:
            print("OVERFLOW!!!")
            exit()
    elif s[:3] == 'for':
        stack.append(int(s.split()[1]))
    else:
        stack.pop()
if len(stack) > 0:
    print("OVERFLOW!!!")
else:
    print(x)