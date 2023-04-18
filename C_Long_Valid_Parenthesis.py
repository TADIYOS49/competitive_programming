s = input().strip()
stack =[]
totalcount = 0
for i in s:
    if i == "(":
        stack.append(i)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
            totalcount += 1
        elif not stack:
            stack.append(i)
        elif stack and stack[-1] == ")":
            stack.append(i)
print(totalcount*2)